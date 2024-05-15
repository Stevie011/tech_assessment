from django.db import models

#simple model to capture user input
class UserDetails(models.Model):
    first_name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return f"First Name : {self.first_name}, Surname : {self.surname}, D.O.B. : {self.date_of_birth} " 