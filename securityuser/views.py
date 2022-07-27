from django.shortcuts import render
from forms.views import my_form
from forms.forms import MyForm
from forms.models import MyModel

def secu(request):
    if request.method == "GET":
        form = MyForm(request.GET)
        if form.is_valid():
            form = MyForm.objects.all()
            print(form)
    else:
        form = MyForm()
    return render(request, 'forms/secur.html', {'form': form})


# Create your views here.
