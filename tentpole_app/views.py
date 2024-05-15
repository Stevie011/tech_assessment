from django.shortcuts import render
from .forms import UserDetailsForm
from .models import UserDetails, IncomeExpenses
from tablib import Dataset
from .resources import ExcelSheetResource


def home_view(request):
    context={}
    
    #this part captures user details
    if 'user_details' in request.POST:
        form = UserDetailsForm(request.POST)
        #built-in checks to see if fields match those specified in the model
        if form.is_valid():
            form.save()
    #file submission
    elif 'file_upload' in request.POST and request.FILES:
        #dataset from tablib
        dataset = Dataset()
        #load the file
        new_sheet = request.FILES['uploaded_file']
        imported_data = dataset.load(new_sheet.read(), format='xlsx')
        for item in imported_data:
            value = IncomeExpenses(
                month=item[0],
                income=item[1],
                expenses=item[2]
            )
            value.save()
        plot_location = plot_graph()
        context["plot_location"] = plot_location
    

    #add the form and saved info to the page context
    context['form'] = UserDetailsForm()
    context['user_details'] = UserDetails.objects.last()
    return render(request, 'home.html', context)


import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from django.templatetags.static import static
from django.conf import settings
import os

def plot_graph():
    #here we reverse the order to get the 12 most recently added
    data = IncomeExpenses.objects.all().order_by('-id')[:12]
    #then we reverse the order of the lists again to get back to the original
    month_list = [item.month for item in data][::-1]
    #convert the numbers from strings to ints for matplotlib
    income_list = [int(item.income) for item in data][::-1]
    expenses_list = [int(item.expenses) for item in data][::-1]
    

    print(month_list)
    print(income_list)
    print(expenses_list)

    plt.plot(month_list, income_list, label='Monthly Income')
    plt.plot(month_list, expenses_list, label='Monthly Expenses')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()

    #print("static root", settings.STATIC_ROOT)


    plot_path = os.path.join(settings.STATIC_ROOT, 'images', 'output_plot.png')
    plot_path_2 = "/Users/steven_stewart/Documents/code/tp tech assessment/tentpole/tentpole_app/static/images/output_plot.png"

    #print("plot path :", plot_path)
    plt.savefig(plot_path)
    plt.savefig(plot_path_2)

    plt.clf()

    return static('images/output_plot.png')

    




