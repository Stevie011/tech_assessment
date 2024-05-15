#standard django render
from django.shortcuts import render
#user details form
from .forms import AllDetailsForm
#models for user details & income/expense data
from .models import UserDetails, IncomeExpenses
#to read the excel data
from tablib import Dataset
#dataframes for easy plotting
import pandas as pd
#to draw the charts
import plotly.express as px

def home_view(request):
    context={}
    #check if a post request with the correct info has been made
    if 'user_details' in request.POST:
        #this part captures user details
        form = AllDetailsForm(request.POST, request.FILES)
        #built-in checks to see if fields match those specified in the model
        if form.is_valid():
            #make sure first letter is uppercase and the rest are lower case
            get_first_name = request.POST.get('first_name')
            first_name_upper = get_first_name[0].upper()+get_first_name[1:].lower()
            get_surname = request.POST.get('surname')
            surname_upper = get_surname[0].upper()+get_surname[1:].lower()

            #create new user model here
            new_user = UserDetails(first_name=first_name_upper, surname=surname_upper, date_of_birth = request.POST.get('date_of_birth'))
            new_user.save()

            #dataset from tablib
            dataset = Dataset()
            #get the uploaded file
            new_sheet = request.FILES['uploaded_file']
            #read the file as a dataset
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
            #draw the graphs
            line_chart, bar_chart = plot_graph()
            #add graphs to context
            context["line_chart"] = line_chart
            context["bar_chart"] = bar_chart
            #add the most recent object to the context
            context['user_details'] = UserDetails.objects.last()

            
    
    #add the form and saved info to the page context
    context['form'] = AllDetailsForm()
    #render the page, along with the context
    return render(request, 'home.html', context)




def plot_graph():
    #here we reverse the order to get the 12 most recently added
    data = IncomeExpenses.objects.all().order_by('-id')[:12]
    #then we reverse the order of the lists again to get back to the original
    month_list = [item.month for item in data][::-1]
    #convert the numbers from strings to ints for plotting
    income_list = [int(item.income) for item in data][::-1]
    expenses_list = [int(item.expenses) for item in data][::-1]
    #save the data as a dictionary
    data = {
        "Month" : month_list,
        "Income" : income_list,
        "Expenses" : expenses_list
    }
    #convert the data to pandas dataframe
    df = pd.DataFrame(data)

    #draw the line chart
    line_plot = px.line(df,
        x='Month',
        y=['Income','Expenses'],
        title="",
        labels={'x': 'Month','y': "Amount"}
    )
    #tweak the appearance
    line_plot.update_layout(title={
        'font_size': 25,
        'xanchor': 'center',
        'x': 0.5,},
        legend_title= "Legend"
    )
    #convert to html for rendering
    line_chart = line_plot.to_html

    #draw the bar chart
    bar_plot = px.bar(df, x='Month', y=['Income', 'Expenses'], barmode='group', 
               color_discrete_map={'Income': 'blue', 'Expenses': 'red'})
    #tweak the appearance
    bar_plot.update_layout(
        title='',
        xaxis_title='Month',
        yaxis_title='Amount',
        legend_title='Category',
        height=400
    )
    #convert to html for rendering
    bar_chart = bar_plot.to_html

    return line_chart, bar_chart




    