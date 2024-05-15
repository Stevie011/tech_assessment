from django import forms

class AllDetailsForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    surname = forms.CharField(max_length=50, required=True)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True)
    uploaded_file = forms.FileField(required=True)
