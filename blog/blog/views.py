from django.http import HttpResponse
from service.models import Service

def say_hello(request):
    service_data = Service.objects.all()
    print(service_data)
    return HttpResponse("Hello World!")

def course_enroller(request, course_id):
    return HttpResponse(f"You are enroled in {course_id}")