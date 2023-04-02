from django.db import  models

class RetailStore(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)


    def register(self):
        self.save()

    def __str__(self):
        return f"{self.name}"