import datetime

def time_remaining(year, month, day):

    userdate = datetime.datetime(year=year, month=month, day=day)

    remaining = userdate - datetime.datetime.now()

    test = ('Faltan {} dias, {} horas y es el dia {} de la semana'.format(remaining.days,int(remaining.seconds / 3600), userdate.weekday()))
    return test

print(time_remaining(2019, 11, 8))