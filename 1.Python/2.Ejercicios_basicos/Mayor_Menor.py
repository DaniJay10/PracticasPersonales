lista = [12, 16, 46, 3, 47, 34, 20]
may = lista[0]
men = lista[0]
for i in range(len(lista)):
    if lista[i] > may:
        may = lista[i]
    elif lista[i] < men:
        men = lista[i]

print(f"El número mayor es: {may}")
print(f"El número menor es: {men}")

