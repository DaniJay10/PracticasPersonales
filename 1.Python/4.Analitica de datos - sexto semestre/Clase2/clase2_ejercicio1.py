n1=int(input("Numero 1:"))
n2=int(input("Numero 2:"))
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
op=int(input("Digite una opcion"))
match op:
    case 1:print("La suma es =",n1+n2)
    case 2:print("La resta es =",n1-n2)
    case 3:print("La multiplicacion es =",n1*n2)
    case 4:
        if n2 != 0:
            print("La division es =",n1/n2)
        else:
            print("operacion no valida")
    case _:print("operacion errada")
    
