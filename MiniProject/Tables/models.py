from pyexpat import model
from django.db import models

class IPC_Sections(models.Model):
    section_number = models.CharField(max_length=50, primary_key=True)
    section_title = models.CharField(max_length = 2000)
    section_description = models.CharField(max_length = 2000)
    section_punishment_description = models.CharField(max_length = 2000)

class IT_Acts(models.Model):
    act_number = models.CharField(max_length=50, primary_key=True)
    act_title = models.CharField(max_length = 2000)
    act_description = models.CharField(max_length = 2000)
    act_punishment_description = models.CharField(max_length = 2000)

class Person_Related(models.Model):
    pr_crime_title = models.CharField(max_length = 2000)
    pr_crime_description = models.CharField(max_length = 2000)
    pr_crime_ipc = models.ForeignKey(IPC_Sections, on_delete=models.CASCADE, default=True, blank=True, null=True)    
    pr_crime_itact = models.ForeignKey(IT_Acts, on_delete=models.CASCADE, default=True, blank=True, null=True)
 
class Government_Related(models.Model):
    gr_crime_title = models.CharField(max_length = 2000)
    gr_crime_description = models.CharField(max_length = 2000)
    gr_crime_ipc = models.ForeignKey(IPC_Sections, on_delete=models.CASCADE, default=True, blank=True, null=True)
    gr_crime_itact = models.ForeignKey(IT_Acts, on_delete=models.CASCADE, default=True, blank=True, null=True)

class Property_Related(models.Model):
    prop_crime_title = models.CharField(max_length = 30)
    prop_crime_description = models.CharField(max_length = 2000)
    prop_crime_ipc = models.ForeignKey(IPC_Sections, on_delete=models.CASCADE, default=True, blank=True, null=True)
    prop_crime_itact = models.ForeignKey(IT_Acts, on_delete=models.CASCADE, default=True, blank=True, null=True)

class IPC_Judgements(models.Model):
    ipc_judgements_title = models.CharField(max_length = 2000, blank=True)
    ipc_judgements_link = models.CharField(max_length = 2000, blank=True)
    ipc_judgement_SC=models.ForeignKey(IPC_Sections,on_delete=models.CASCADE)

class IT_Judgements(models.Model):
    it_judgements_title = models.CharField(max_length = 2000, blank=True)
    it_judgements_link = models.CharField(max_length = 2000, blank=True)
    it_judgement_SC=models.ForeignKey(IT_Acts,on_delete=models.CASCADE, blank=True, default=True)