from django.http import HttpResponse
import datetime


# Настройте приложение из второго задания, чтобы оно выводило в браузер текущую дату и время.
def current_date_time(request):
    current_datetime = datetime.datetime.now()
    datetime_string = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(datetime_string)


# Создайте веб-приложение, отображающее таблицу умножения от 1 до 10.
def multiply(request):
    multi_table = ''
    for i in range(1, 11):
        for j in range(1, 11):
            multi_table += f'<p>{i} * {j} = {i * j}<p>'
    return HttpResponse(multi_table)


def multiply_(request, wrong):
    return multiply(request)

# Создайте веб-приложение, отображающее дату дня программиста в текущем году. День программиста — 256-й день года.
def programmers_day(request):
    today = datetime.date.today()
    first_day_year = datetime.date(today.year, 1, 1)
    delta = datetime.timedelta(days=256)
    prog_day = first_day_year + delta
    return HttpResponse(f'День программиста в этом году - {prog_day.day}.{prog_day.month}.{prog_day.year}')


def programmers_day_(request, wrong):
    return programmers_day(request)