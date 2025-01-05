n1=int(input("Numero 1:"))
n2=int(input("Numero 2:"))
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
op=int(input("Digite una opcion"))
if op==1:
    print("La suma es =",n1+n2)
elif op==2:
    print("La resta es =",n1-n2)
elif op==3:
    print("La multiplicacion es =",n1*n2)
elif op==4:
    if n2 != 0:
        print("La division es =",n1/n2)
    else:
        print("operacion no valida")
else:
    print("operacion errada")
