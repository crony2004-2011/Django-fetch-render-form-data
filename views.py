from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from .models import survey
from .forms import queryform

# Create your views here.
def home(request,name):
    time = datetime.datetime.now();
    return render(request, 'wel.html', {'time':time,'name':name})

def query(request):
    context ={}
    entries = survey.objects.all()
    form = queryform(request.POST)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, 'query.html', {'form': form,'entries':entries})

#def all(request):
 #   entries = survey.objects.all()
  #  return render(request, 'query.html', {'entries': entries})







