segundos = int(input("Digite os segundos que você quer converter: "))

dias = segundos // 86400
segundos_restantes = segundos % 86400
horas = segundos_restantes // 3600
segundos_restantes = segundos_restantes % 3600
minutos = segundos_restantes // 60
segundos_restantes = segundos_restantes % 60

print("{} dias, {} horas, {} minutos e {} segundos." .format(dias, horas, minutos, segundos_restantes))