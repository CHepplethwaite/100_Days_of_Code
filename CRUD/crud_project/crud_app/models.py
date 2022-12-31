from django.db import models

class PatientInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.DecimalField(max_digits=3, decimal_places=0)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    comment = models.TextField(max_length=50)
    image = models.ImageField(upload_to="crud_app/static/", blank=True)
    national_id = models.CharField(max_length=50,primary_key=False)

    def __str__(self) -> str:
        return self.last_name