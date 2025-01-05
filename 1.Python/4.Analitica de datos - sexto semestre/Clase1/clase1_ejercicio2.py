ParcialU = float(input("Digite nota parcial 1: "))
ParcialD = float(input("Digite nota parcial 2: "))
ParcialT = float(input("Digite nota parcial 3: "))

definitiva = (ParcialU*25/100) + (ParcialD*35/100) + (ParcialT*40/100)

if definitiva > 3:
    print("Aprobó la materia, su nota es:", definitiva)
else:
    print("Reprobó la materia, su nota es:", definitiva)


