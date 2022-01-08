from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
list_days = {
    1 : "monday",
    2 : "tuesday",
    3 : "Wednesday",
    4 : "Thursday",
    5 : "Friday",
    6 : "Saturday",
    7 : "Sunday"
}
def list_todo(request, day):
    day = day.lower()
    return render(request, 'week_days/greeting.html')
    # elif day == 'tuesday':
    #     return HttpResponse(f"""
    #     <h1> Список дел в {day} </h1>
    #      <ul>
    #      <li> Дело №1 </li> <li> Дело №2 </li>
    #      </ul>
    # """)
    # else:
    #     return HttpResponseNotFound(f'Дел в {day} не найдено')

def list_todo_num(request, day:int):
    if day > 0 and day <= 7:
        name_day = list_days.get(day)
        redirect_url = reverse("todo_week-name", args=(name_day, ))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f"Неверный номер дня - {day}")