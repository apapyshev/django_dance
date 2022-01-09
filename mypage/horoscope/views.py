from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
list_zodiac = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'
}

sign_dates = (
    ((20, 3), (19, 4)),  # Aries
    ((20, 4), (20, 5)),
    ((21, 5), (20, 6)),
    ((21, 6), (22, 7)),
    ((23, 7), (22, 8)),
    ((23, 8), (22, 9)),
    ((23, 9), (22, 10)),
    ((23, 10), (21, 11)),
    ((22, 11), (21, 12)),
    ((22, 12), (19, 1)),
    ((20, 1), (17, 2)),
    ((18, 2), (19, 3)),  # Pisces
)

elements = {
    'fire' : ['aries', 'leo', 'sagittarius'],
    'earth' : ['taurus', 'virgo', 'capricorn'],
    'air' : ['gemini', 'libra', 'aquarius'],
    'water' : ['cancer', 'scorpio', 'pisces']
}

def index(request):
    zodiacs = list(list_zodiac.keys())
    # li_zodiac += f"<li> <a href = '{redirect_path}'>{_.title()} </a></li>"
    context = {
       'zodiacs':zodiacs,
        'list_zodiac': list_zodiac
    }
    return render(request, 'horoscope/index.html', context=context)

def zodiac_sign_get_info(request, zodiac_sign:str):
    description = list_zodiac.get(zodiac_sign)
    zodiacs = list(list_zodiac.keys())
    data = {
        'description_zodiac': description,
        'sign': zodiac_sign,
        'sign_name': description.split()[0],
        'zodiacs': zodiacs
    }
    return render(request, 'horoscope/info_zodiak.html', context=data)

def zodiac_sign_get_info_num(request, zodiac_sign:int):
    if zodiac_sign > 12:
        return HttpResponseNotFound(f"Нет такого знака зодиака")
    else:
        zodiak = list(list_zodiac.keys())[zodiac_sign - 1]
        redirect_url = reverse("horoscope-name", args=(zodiak, ))
        return HttpResponseRedirect(redirect_url)

def types_zodiac(request):
    el = list(elements.keys())
    li_el = ''
    for val in el:
        redirect_path = reverse("horoscope-types", args=(val,))
        li_el += f"<li> <a href = '{redirect_path}'>{val.title()} </a></li>"
    responce_url = f"""
    <ul>
    {li_el}
    </ul>
    """
    return HttpResponse(responce_url)

def types_element(request, type):
    el = elements.get(type)
    li_el = ""
    for val in el:
        redirect_path = reverse("horoscope-name", args=(val, ))
        li_el += f"<li> <a href = '{redirect_path}'>{val.title()} </a></li>"
    responce_url = f"""
    <ul>
    {li_el}
    </ul>
    """
    return HttpResponse(responce_url)


def get_about_from_date(request, month, day):
    index_zodiak = 0
    for el in sign_dates: #    ((20, 3), (19, 4)),  # Aries
        if month >= el[0][1] and month <= el[1][1]:
            if day >= el[0][0] and day <= el[1][0]:
                index_zodiak = sign_dates.index(el)
    redirect_responce = reverse('horoscope-number', args=(index_zodiak,))
    return HttpResponseRedirect(redirect_responce)
