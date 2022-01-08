from django.urls import path
from week_days import views as views_week_days

urlpatterns = [
    path('<int:day>/', views_week_days.list_todo_num, ),
    path('<int:day>', views_week_days.list_todo_num),
    path('<str:day>/', views_week_days.list_todo, name="todo_week-name"),
    path('<day>', views_week_days.list_todo),
    ]