from django.db import models
from django.core.serializers.json import DjangoJSONEncoder


#simple model to capture user input
class UserDetails(models.Model):
    first_name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    date_of_birth = models.DateField()
    data_frame = models.JSONField(encoder=DjangoJSONEncoder)





