from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    print("say somehing")
    return render(request, "index.html")

def say_hello(request):
    return HttpResponse("Hello World!")

def course_enroller(request, course_id):
    return HttpResponse(f"You are enroled in {course_id}")