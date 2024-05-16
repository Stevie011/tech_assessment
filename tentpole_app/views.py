#standard django render
from django.shortcuts import render
#user details form
from .forms import AllDetailsForm
#models for user details & income/expense data
from .models import UserDetails
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

    
            new_sheet = request.FILES['uploaded_file']
            #convert sheet direclty to dataframe
            df_test = pd.read_excel(new_sheet, engine='openpyxl')

            df_json = df_test.to_json()

            #create new user model here
            new_user = UserDetails(first_name=first_name_upper, surname=surname_upper, date_of_birth = request.POST.get('date_of_birth'), data_frame=df_json)
            new_user.save()
            #draw the graphs
            line_chart, bar_chart = plot_graph(df_test)
            #add graphs to context
            context["line_chart"] = line_chart
            context["bar_chart"] = bar_chart
            #add the most recent object to the context
            context['user_details'] = UserDetails.objects.last()

            
    
    #add the form and saved info to the page context
    context['form'] = AllDetailsForm()
    #render the page, along with the context
    return render(request, 'home.html', context)




def plot_graph(dataframe):

    #draw the line chart
    line_plot = px.line(dataframe,
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
    bar_plot = px.bar(dataframe, x='Month', y=['Income', 'Expenses'], barmode='group', 
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




    