import datetime

def past_time(year, month, day):
    user_date = datetime.datetime(year=year, month=month, day=day,)
    entorno = datetime.datetime.now() - user_date


    return 'Han pasado {} horas'.format(int(entorno.total_seconds() / 3600))

print(past_time(2018, 11, 8))