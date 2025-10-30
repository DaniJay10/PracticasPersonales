# Daniel Pinzon Jay - ELectiva III

X = [8,12,11,15,22,26,25,28,35]

# 1. Calular la suma de los numeros pares del array X
cont = 0
for num in X:
    if num % 2 == 0:
        cont += num
print("1. Suma de los numeros pares:", cont)

# 2. Determinar el valor de la ecuacion y=3x+8 para cada valor del array X
y = []
for num in X:
    y.append(3 * num + 8)
    print("2. Valor de la ecuacion y=3x+8 para el valor X=", num, "es:", 3 * num + 8)

#3. Calcular el cuadrado de cada valor impar del array X
for num in X:
    if num % 2 != 0:
        print("3. El cuadrado de", num, "es:", num ** 2)

#4. Calcular para cada valor del array X, el calculo de x-promedio
promedio = sum(X) / len(X)
for num in X:
    print("4. El valor de", num, "menos el promedio es:", num - promedio)
