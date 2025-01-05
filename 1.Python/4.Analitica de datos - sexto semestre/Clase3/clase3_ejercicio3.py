n1=int(input("Numero 1:"))
n2=int(input("Numero 2:"))
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
op=int(input("Digite una opcion"))
def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicacion(a,b):
    return a*b
def division(a,b):
    if b != 0:
        return a/b
    else:
        return("operacion no valida")

match op:
    case 1:print("La suma es =",suma(n1,n2))
    case 2:print("La resta es =",resta(n1,n2))
    case 3:print("La multiplicacion es =",multiplicacion(n1,n2))
    case 4:print("La division es =",division(n1,n2))
    case _:print("operacion errada")
