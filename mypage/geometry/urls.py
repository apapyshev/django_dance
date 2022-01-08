from django.urls import path
from geometry import views

urlpatterns = [
    path('get_rectangle_area/<int:width>/<int:height>', views.redirect_get_rectangle_area),
    path('get_square_area/<int:width>', views.redirect_get_square_area),
    path('get_circle_area/<int:radius>', views.redirect_get_circle_area),
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area),
    path('square/<int:width>', views.get_square_area),
    path('circle/<int:radius>', views.get_circle_area),
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area, name="redirect-rectangle-name"),
    path('square/<int:width>/', views.get_square_area, name="redirect-square-name"),
    path('circle/<int:radius>/', views.get_circle_area, name="redirect-circle-name"),
]