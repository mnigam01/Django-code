from django.shortcuts import render
from django.http import HttpResponse
from service.models import Service

# Create your views here.
def fetch_service(request, slug):
    data = Service.objects.filter(service_slug = slug)
    return HttpResponse(data)
    
