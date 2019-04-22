import datetime
import random

AVERAGE_LIFESPAN = 80

SMOKER_PENALIZATION = 10
DRINKER_PENALIZATION = 10
SEDENTARY_PENALIZATION = 20


def print_with_underscores(message):
    print(message)
    print(len(message) * '-')


def ask_yes_or_no(message):
    response = None
    while (response != 'S' and response != 'N') and response != 'A':
        response = input(message + "[S/N/A]").upper()

    return response 



print_with_underscores('Averigua cuanto te queda de vida!')

print('Completa esta encuesta para saber cuanto tiempo te queda de vida!')

birth_date = input('Cual es tu fecha de nacimiento(dd/mm/yyyy)?: ')
birth_date = datetime.datetime.strptime(birth_date, "%d/%m/%Y")

years_lost = 0

if ask_yes_or_no("Fumas?") == 'S':
    years_lost += SMOKER_PENALIZATION
elif 'A':
    years_lost += (SMOKER_PENALIZATION / 2)

if ask_yes_or_no("Tomas alcohol?") == 'S':
    years_lost += DRINKER_PENALIZATION
elif 'A':
    years_lost += (DRINKER_PENALIZATION / 2)

if ask_yes_or_no("Haces ejercicios?") != 'S':
    if 'N':
        years_lost += SEDENTARY_PENALIZATION
    elif 'A':
        years_lost += (SEDENTARY_PENALIZATION / 2)

base_lifespan = random.randint(AVERAGE_LIFESPAN / 2, AVERAGE_LIFESPAN)
lifespan = base_lifespan - years_lost
death_day = birth_date + datetime.timedelta(days=lifespan * 365)
days_to_death = death_day - datetime.datetime.now()

print("La fecha de tu muerte {}, te quedan {} dias de vida ".format(death_day.strftime("%d/%m/%Y"), days_to_death.days))
print(years_lost)
