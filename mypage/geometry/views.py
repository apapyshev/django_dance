from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse

# Create your views here.

def get_rectangle_area(request, width, height):
    # return HttpResponse(f"Площадь прямоугольника размером {width}х{height} равна {width*height}")
    return render(request, 'geometry/rectangle.html')

def get_square_area(request, width):
    # return HttpResponse(f"Площадь квадрата размером {width} равна {width*width}")
    return render(request, 'geometry/square.html')

def get_circle_area(request, radius):
    # return HttpResponse(f"Площадь круга радиусом {radius} равна {round(pi * radius * radius, 2)}")
    return render(request, 'geometry/circle.html')

def redirect_get_rectangle_area(request, width, height):
    redirect_url = reverse("redirect-rectangle-name", args=(width, height,))
    return HttpResponseRedirect(redirect_url)

def redirect_get_square_area(request, width):
    redirect_url = reverse("redirect-square-name", args=(width, ))
    return HttpResponseRedirect(redirect_url)

def redirect_get_circle_area(request, radius):
    redirect_url = reverse("redirect-circle-name", args=(radius, ))
    return HttpResponseRedirect(redirect_url)
