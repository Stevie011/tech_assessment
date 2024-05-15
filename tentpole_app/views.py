from django.shortcuts import render
from .forms import UserDetailsForm
from .models import UserDetails, IncomeExpenses
from tablib import Dataset
from .resources import ExcelSheetResource


def home_view(request):
    context={}
    if request.method == 'POST':
        #call the from in forms.py
        form = UserDetailsForm(request.POST, request.FILES)
        #built-in checks to see if fields match those specified in the model
        if form.is_valid():
            


            form.save()
        excel_sheet_resource = ExcelSheetResource()
        dataset = Dataset()
        new_sheet = request.FILES['uploaded_file']
        imported_data = dataset.load(new_sheet.read(), format='xlsx')
        for item in imported_data:
            value = IncomeExpenses(
                month=item[0],
                income=item[1],
                expenses=item[2]
            )
            value.save()
    else:
        form = UserDetailsForm()

    #add the form and saved info to the page context
    context['form'] = form
    context['user_details'] = UserDetails.objects.last()
    return render(request, 'home.html', context)



# def import_excel(request):
#     if request.method == 'POST':
#         pass
#     return render(request, 'index.html')

