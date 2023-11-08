from django.db import models


# Create your models here.
class Hospital_Doctors_info(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    department = models.CharField(max_length=250)
    specialization = models.CharField(max_length=250)
    email = models.EmailField(null=True)
    phone_number = models.IntegerField(default=None,null=True)

    class Meta:
        db_table = 'doctors_profile'

    def __str__(self):
        return self.name
