zona1=500000
zona2=700000
zona3=900000

zona=int(input("digite su zona"))
genero=input("digite su genero")
estrato=int(input("digite su estrato"))

match zona:
    case 1:print("Bono: ",zona1)
    case 2:print("Bono: ",zona2)
    case 3:
        if(genero == "Mujer" and (estrato == 1 or estrato == 2)):
            print("Bono: ",zona3+1000000)
        else:
            print("Bono: ",zona3)
