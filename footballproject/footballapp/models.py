from django.db import models

# Create your models here.
class Football(models.Model):
    team_name=models.CharField(max_length=250)
    coach_name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):

        return self.team_name
