from django.db import models

class UserInformation(models.Model):
    gender_choices = models.TextChoices('GenderType', 'Male Female Other')

    name = models.CharField(max_length = 200)
    age = models.IntegerField()
    gender = models.CharField(choices = gender_choices.choices, max_length=15)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
     

class UserHappinessData(models.Model):
    user = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    date = models.DateField(primary_key=True)
    sleep = models.FloatField()
    exercise = models.FloatField()
    social = models.FloatField()
    metime = models.FloatField()
    weather = models.FloatField()
    socialmedia = models.FloatField()
    happy = models.IntegerField()






