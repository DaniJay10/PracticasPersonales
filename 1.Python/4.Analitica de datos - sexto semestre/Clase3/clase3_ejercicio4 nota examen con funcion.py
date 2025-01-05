#hacer un programa que permita crear una funcion para calcular la nota definitiva
#del estudiante si tiene el primer parcial del 20%, el segundo del 35% y
#y el examen de 45%. Debe decir si aprobo o no aprobo

def nota(p1,p2,p3):
    Definitiva = (p1*0.20)+(p2*0.35)+(p3*0.45)
    if Definitiva >= 3:
        return"El estudiante aprobo con nota: ",Definitiva
    else:
        return"El estudiante desaprobo con nota: ",Definitiva
    
nota1 = float(input("Ingrese la nota del primer parcial"))  
nota2 = float(input("Ingrese la nota del segundo parcial"))
nota3 = float(input("Ingrese la nota del tercer parcial"))
print(nota(nota1,nota2,nota3))
