from django.db import models

#simple model to capture user input
class UserDetails(models.Model):
    first_name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    date_of_birth = models.DateField()

#model with fields for each entry in the file    
class IncomeExpenses(models.Model):
    month = models.CharField(max_length=20)
    income = models.CharField(max_length=20)
    expenses = models.CharField(max_length=20)



