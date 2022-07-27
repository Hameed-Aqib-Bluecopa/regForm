from django import forms
from .models import MyModel
from django.forms import TextInput
from django import forms
 
class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["fullname","gender", "mobile_number","email","company_name","visit_date","id_proof","id_number",]
    labels = {'fullname': "Name",
              'gender':'Gender',
              "mobile_number": "Mobile Number",
              "email": "Email",
              "company_name":"Company Name",
              "visit_date" : "Visit Date",
              "id_proof" : "ID Proof",
              "id_number" : "ID Number",
            }
    widgets = {
            'fullname': TextInput(attrs={'placeholder': 'Enter Your Name'}),
            'mobile_number': TextInput(attrs={'placeholder': 'Enter Your Mobile No.'}),
            'email': TextInput(attrs={'placeholder': 'Enter Your Email'}),
            'company_name': TextInput(attrs={'placeholder': 'Enter Your Company Name'}),
            'visit_date': TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'id_number': TextInput(attrs={'placeholder': 'ID Number'}),
        }