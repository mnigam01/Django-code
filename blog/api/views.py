from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def home(request):
    return Response({'status':200,'message':'Successfully done!!'})
