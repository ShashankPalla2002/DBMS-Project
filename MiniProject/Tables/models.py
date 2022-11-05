from pyexpat import model
from django.db import models

class Person_Related(models.Model):
    pr_crime_title = models.CharField(max_length = 30)
    pr_crime_description = models.CharField(max_length = 100)

class Government_Related(models.Model):
    gr_crime_title = models.CharField(max_length = 30)
    gr_crime_description = models.CharField(max_length = 100)

class Property_Related(models.Model):
    prop_crime_title = models.CharField(max_length = 30)
    prop_crime_description = models.CharField(max_length = 100)

class IPC_Sections(models.Model):
    section_number = models.CharField(max_length=50, primary_key=True)
    section_title = models.CharField(max_length = 100)
    section_description = models.CharField(max_length = 100)
    section_punishment_description = models.CharField(max_length = 100)

class IT_Acts(models.Model):
    act_number = models.IntegerField
    act_title = models.CharField(max_length = 100)
    act_description = models.CharField(max_length = 100)
    act_punishment_description = models.CharField(max_length = 100)

class Judgements(models.Model):
    judgements_description = models.CharField(max_length = 100)
    judgement_SC=models.ForeignKey(IPC_Sections,on_delete=models.CASCADE)