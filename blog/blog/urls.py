"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import say_hello, course_enroller, home


# important materiall for study
# https://docs.djangoproject.com/en/5.0/topics/http/urls/
# read section path converters

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('hello/', say_hello),
    path('course/<slug:course_id>', course_enroller)
]
