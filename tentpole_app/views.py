from django.shortcuts import render
from .forms import UserDetailsForm
from .models import UserDetails, IncomeExpenses
from tablib import Dataset
import pandas as pd

import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
from django.templatetags.static import static
from django.conf import settings
import os
import plotly.express as px


def home_view(request):
    context={}
    
    #this part captures user details
    if 'user_details' in request.POST:
        form = UserDetailsForm(request.POST)
        #built-in checks to see if fields match those specified in the model
        if form.is_valid():
            context['user_details'] = UserDetails.objects.last()

            form.save()
    #file submission
    elif 'file_upload' in request.POST and request.FILES:
        #dataset from tablib
        dataset = Dataset()
        #get the file
        new_sheet = request.FILES['uploaded_file']
        #load the file as a dataset
        imported_data = dataset.load(new_sheet.read(), format='xlsx')
        #iterate through data
        for item in imported_data:
            #add fields as per model
            value = IncomeExpenses(
                month=item[0],
                income=item[1],
                expenses=item[2]
            )
            value.save()
        line_chart, bar_chart = plot_graph()
        context['user_details'] = UserDetails.objects.last()

        context["line_chart"] = line_chart
        context["bar_chart"] = bar_chart
    

    #add the form and saved info to the page context
    context['form'] = UserDetailsForm()
    #context['user_details'] = UserDetails.objects.last()
    return render(request, 'home.html', context)




def plot_graph():
    #here we reverse the order to get the 12 most recently added
    data = IncomeExpenses.objects.all().order_by('-id')[:12]
    #then we reverse the order of the lists again to get back to the original
    month_list = [item.month for item in data][::-1]
    #convert the numbers from strings to ints for matplotlib
    income_list = [int(item.income) for item in data][::-1]
    expenses_list = [int(item.expenses) for item in data][::-1]

    data = {
        "Month" : month_list,
        "Income" : income_list,
        "Expenses" : expenses_list
    }

    df = pd.DataFrame(data)

    # print("months :", month_list)
    # print("income :", income_list)
    # print("expenses :", expenses_list)

    line_plot = px.line(df,
        x='Month',
        y=['Income','Expenses'],
        title="Income vs Expenditure (Plotly)",
        labels={'x': 'Month','y': "Amount"}
    )

    line_plot.update_layout(title={
        'font_size': 25,
        'xanchor': 'center',
        'x': 0.5,},
        legend_title= "Legend"
    )

    line_chart = line_plot.to_html

    bar_plot = px.bar(df, x='Month', y=['Income', 'Expenses'], barmode='group', 
               color_discrete_map={'Income': 'blue', 'Expenses': 'red'})
    
    bar_plot.update_layout(
        title='Income vs Expenses',
        xaxis_title='Month',
        yaxis_title='Amount',
        legend_title='Category',
        height=400
    )
    
    bar_chart = bar_plot.to_html

    return line_chart, bar_chart




    




