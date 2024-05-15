from django.db import models
from import_export import resources

#simple model to capture user input
class UserDetails(models.Model):
    first_name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    #excel_sheet = models.FileField()
    
    def __str__(self):
        return f"First Name : {self.first_name}, Surname : {self.surname}, D.O.B. : {self.date_of_birth} " 
    
class IncomeExpenses(models.Model):
    month = models.CharField(max_length=20)
    income = models.CharField(max_length=20)
    expenses = models.CharField(max_length=20)



# class ExcelSheetResource(resources.ModelResource):
#     class Meta:
#         model = IncomeExpenses
#         import_id_fields = ["month", "income", "expenses"]
#         skip_unchanged = True
#         use_bulk = True