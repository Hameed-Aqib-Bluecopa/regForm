from django.shortcuts import render
from .models import MyModel
from .forms import MyForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .serializers import HeroSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
import smtplib
import random
gmail_user = 'demobluecopa@gmail.com'
gmail_password = 'jcgogplflvassjlz'
#gmail_password is not your actual password it is your app password
#app password can be generated using google account settings
sent_from = gmail_user
#to = ['mohammed.abdul@bluecopa.com', 'chandu.thota@bluecopa.com']
#subject = 'Test Mail 2'
#body = 'This is a Test Mail 2'

otp = random.randint(0,999999)


class MyModelViewSet(viewsets.ModelViewSet):
    queryset = MyModel.objects.all().order_by('fullname')
    serializer_class = HeroSerializer

def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
      fname= form.cleaned_data.get("fullname")
      gen = form.cleaned_data.get("gender")
      mnumber = form.cleaned_data.get("mobile_number")
      email = form.cleaned_data.get("email")
      cname = form.cleaned_data.get("company_name")
      vdate = form.cleaned_data["visit_date"]
      idp = form.cleaned_data.get("id_proof")
      idn = form.cleaned_data.get("id_number")
      form = MyForm()
      #print(fname)
      to = [email]
      subject = 'OTP for Registration'
      body = 'The OTP for your Registration at T-Hub 2.0 is ',otp
      email_text = """\
      From: %s
      To: %s
      Subject: %s

      %s
      """ % (sent_from, ", ".join(to), subject, body)
      try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
      except Exception as ex:
          print ("Something went wrong….",ex)


      return HttpResponseRedirect(reverse('home'))
  else:
      form = MyForm()
  return render(request, 'forms/index.html', {'form': form})
@api_view(['GET'])
def getData(request):
  form = MyForm.objects.all()
  serializer = HeroSerializer(form, many = True)
  return Response(serializer.data)

# Create your views here.
