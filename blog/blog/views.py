from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        "heading" : "This is a new heading"
    }
    return render(request, "index.html", data)

def say_hello(request):
    return HttpResponse("Hello World!")

def course_enroller(request, course_id):
    return HttpResponse(f"You are enroled in {course_id}")