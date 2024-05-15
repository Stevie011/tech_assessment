from django import forms

from .models import UserDetails, IncomeExpenses

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"

class ExcelSheetForm(forms.Form):
    class Meta:
        model = IncomeExpenses
        fields = "__all__"