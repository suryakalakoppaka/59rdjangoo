from django.db import models


class students(models.Model):
    std_id=models.IntegerField()
    std_name=models.CharField(max_length=50)
    std_age=models.IntegerField()
