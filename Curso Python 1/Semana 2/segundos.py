entradas = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = (entradas//(3600*24))
horas = (entradas%(3600*24))//3600
minutos = (entradas % 3600)//60
segundos = (entradas % 3600) % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos,"segundos.")