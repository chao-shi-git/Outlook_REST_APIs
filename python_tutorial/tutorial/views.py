from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
  return HttpResponse("Welcome to the tutorial.")