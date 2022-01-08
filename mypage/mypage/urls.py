"""mypage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from horoscope import views as views_horoscope
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/', views_horoscope.index),
    path('horoscope/types/', views_horoscope.types_zodiac),
    path('horoscope/types/<str:type>', views_horoscope.types_element, name="horoscope-types"),
    path('horoscope/<int:month>/<int:day>', views_horoscope.get_about_from_date, name="horoscope-date"),
    path('horoscope/<int:zodiac_sign>', views_horoscope.zodiac_sign_get_info_num, name="horoscope-number"),
    path('horoscope/<int:zodiac_sign>/', views_horoscope.zodiac_sign_get_info_num, name="horoscope-number"),
    path('horoscope/<str:zodiac_sign>', views_horoscope.zodiac_sign_get_info, name="horoscope-name"),
    path('horoscope/<str:zodiac_sign>/', views_horoscope.zodiac_sign_get_info, name="horoscope-name"),
    path('todo_week/', include('week_days.urls')),
    path('calculate_geometry/', include('geometry.urls')),
]
