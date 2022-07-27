from django.db import models
from django import forms

gen_choices = (
    ('-','------'),
    ('male','Male'),
    ('female','Female'),
    ('not specify','Not Specify')
)
id_choices = (
    ('-','-----'),
    ('aadhaar','Aadhaar Card'),
    ('passport','Passport'),
    ('pan','PAN Card'),
    ('voterid','Voter ID'),
    ('dlicense','Driving License')
)
class MyModel(models.Model):
    fullname = models.CharField(max_length=40)
    gender = models.CharField(max_length=20,choices = gen_choices,default = '-')
    mobile_number = models.IntegerField()
    email = models.EmailField()
    company_name = models.CharField(max_length=20)
    visit_date = models.DateField()
    id_proof = models.CharField(max_length=30,choices = id_choices,default = '-')
    id_number = models.CharField(max_length=30)



# Create your models here.
