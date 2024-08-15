from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("Hello World!")

def course_enroller(request, course_id):
    return HttpResponse(f"You are enroled in {course_id}")