import math
pi = math.pi
print("-----------------Menu de areas, perimetros y volumenes-----------------")
#areas
def AreaTriangulo(b,a):
    area = 1/2*b*a
    return "El area del triangulo es:" + str(area)

def AreaCirculo(r):
    area = pi*r**2
    return "El area del circulo es:" + str(area)

def AreaCuadrado(l):
    area = l**2
    return "El area del cuadrado es:" + str(area)

def AreaPentagono(l):
    area = 1/4 * (5*(5+2*5**(1/2)))**(1/2) * l**2
    return "El area del cuadrado es:" + str(area)

def AreaRombo(d1,d2):
    area = (d1*d2)/2
    return "El area del rombo es:" + str(area)

def areaHexagono(l):
    area = (3*3**(1/2)*l**2)/2
    return "El area del hexagono es:" + str(area)





#perimetros
def PerimetroTriangulo(l1,l2,l3):
    perimetro = l1+l2+l3
    return "El perimetro del triangulo es:" + str(perimetro)

def PerimetroRombo(l):
    perimetro = 4*l
    return "El perimetro del Rombo es:" + str(perimetro)

def PerimetroCuadrado(l):
    perimetro = 4*l
    return "El perimetro del cuadrado es:" + str(perimetro)

def PerimetroHexagono(l):
    perimetro = 6*l
    return "El perimetro del hexagono es:" + str(perimetro)





#volumenes
def VolumenCubo(l):
    volumen = l**3
    return "El volumen del cubo es:" + str(volumen)

def VolumenEsfera(r):
    volumen = 4/3 * pi * r**3
    return "El volumen de la esfera es:" + str(volumen)

def VolumenPiramide(b,a,h):
    volumen = 1/3 * (1/2*b*a) * h
    return "El volumen de la piramide triangular es:" + str(volumen)

def VolumenCono(r,a):
    volumen = 1/3 * pi * r**2 * a
    return "El volumen del cono es:" + str(volumen)




#menu
while True:
    print("1. Áreas")
    print("2. Perímetros")
    print("3. Volúmenes")
    print("4. Salir")
    op = int(input("Elige una opción: "))
    match op:
        #areas
        case 1:
            print("1. Area del triangulo")
            print("2. Area del circulo")
            print("3. Area del cuadrado")
            print("4. Area del pentagono")
            print("5. Area del rombo")
            print("6. Area del exagono regular")
            print("7. salir")
            opArea = int(input("Elige una opción: "))
            match opArea:
                case 1:
                    base=float(input("Ingrese base triangulo"))
                    altura=float(input("Ingrese altura triangulo"))
                    print(AreaTriangulo(base,altura))
                case 2:
                    radio=float(input("Ingrese radio circulo"))
                    print(AreaCirculo(radio))
                case 3:
                    lado=float(input("Ingrese longitud de un lado del cuadrado"))
                    print(AreaCuadrado(lado))
                case 4:
                    lado=float(input("Ingrese longitud de un lado del pentagono"))
                    print(AreaPentagono(lado))
                case 5:
                    lado1=float(input("Ingrese longitud diagonal 1 del rombo"))
                    lado2=float(input("Ingrese longitud diagonal 2 del rombo"))
                    print(AreaRombo(lado1,lado2))
                case 6:
                    lado=float(input("Ingrese longitud de un lado del Hexagono"))
                    print(AreaHexagono(lado))
                case 7:
                    continue
                case _:
                    print("Opcion no valida")
        #volumenes
        case 2:
            print("1. Perimetro del triangulo")
            print("2. Perimetro del rombo")
            print("3. Perimetro del cuadrado")
            print("4. Perimetro del exagono")
            print("5. salir")
            opPe = int(input("Elige una opción: "))
            match opPe:
                case 1:
                    lado1=float(input("Ingrese lado 1 del triangulo"))
                    lado2=float(input("Ingrese lado 2 del triangulo"))
                    lado3=float(input("Ingrese lado 3 del triangulo"))
                    print(PerimetroTriangulo(lado1,lado2,lado3))
                case 2:
                    lado=float(input("Ingrese longitud de un lado del rombo"))
                    print(PerimetroRombo(lado))
                case 3:
                    lado=float(input("Ingrese longitud de un lado del Cuadrado"))
                    print(PerimetroCuadrado(lado))
                case 4:
                    lado=float(input("Ingrese longitud de un lado del hexagono"))
                    print(PerimetroHexagono(lado))
                case 5:
                    continue
                case _:
                    print("Opcion no valida")
        #volumenes
        case 3:
            print("1. volumen del cubo")
            print("2. Volumen de la esfera")
            print("3. Volumen de la piramide triangular")
            print("4. Volumen del cono")
            print("5. salir")
            opVol = int(input("Elige una opción: "))
            match opVol:
                case 1:
                    lado=float(input("Ingrese longitud de un lado del cubo"))
                    print(VolumenCubo(lado))
                case 2:
                    radio=float(input("Ingrese radio de la esfera"))
                    print(VolumenEsfera(lado))
                case 3:
                    baseT=float(input("Ingrese base triangular"))
                    alturaT=float(input("Ingrese altura triangular"))
                    alturaP=float(input("Ingrese altura piramide"))
                    print(VolumenPiramide(baseT,alturaT,alturaP))
                case 4:
                    radio=float(input("Ingrese radio base del cono"))
                    altura=float(input("Ingrese altura del cono"))
                    print(VolumenCono(radio,altura))
                case 5:
                    continue
                case _:
                    print("Opcion no valida")
        #salida
        case 4:
            print("Gracias por usarnos")
            break
        case _:
            print("Opcion no valida")
            
            

        







