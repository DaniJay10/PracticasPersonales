cont=0;
acum=0;
cant=int(input("Cantidad de numeros: ->"))
while cont<cant:
    cont+=1
    acum+=cont
    print(cont)
prom=acum/cant
print("La sumatoria es:", acum)
print("El promedio es:", prom)
