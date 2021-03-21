from django.db import models

# Create your models here.


class AddContact(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    company = models.CharField(max_length=150, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return self.name
