import datetime

tiempo_atras = datetime.datetime.now() - datetime.timedelta(days=5)

print("Hace 5 dias fue {}".format(tiempo_atras.strftime('%d de %m del %Y')))