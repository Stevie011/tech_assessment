from django.shortcuts import render
from .forms import UserDetailsForm
from .models import UserDetails

def home_view(request):
    context={}
    #call the from in forms.py
    form = UserDetailsForm(request.POST or None)
    #built-in checks to see if fields match those specified in the model
    if form.is_valid():
        form.save()
    #add the form and saved info to the page context
    context['form'] = form
    context['user_details'] = UserDetails.objects.last()
    return render(request, 'home.html', context)

