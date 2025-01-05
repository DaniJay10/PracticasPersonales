i=0
j=0
while i<10:
    i+=1
    while i<10:
        i+=1
        while j<10:
            j+=1
            print(f"{i} x {j} =",i*j)
        print("-------------------------------")
        j=0
