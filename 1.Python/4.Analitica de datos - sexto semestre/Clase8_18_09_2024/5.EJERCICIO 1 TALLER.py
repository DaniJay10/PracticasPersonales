import matplotlib.pyplot as plt
valor1=int(input("Digite valor inicio x"))
valor2=int(input("Digite valor fin x"))
y=[]
x=range(valor1,valor2,1)
for i in x:
    y.append((2*i**3) + (3*i))    # Calculamos y=2x^3 + 3x

plt.plot(x,y)
plt.title("FUNCION Y=2X^3 + 3X")
plt.xlabel("X")
plt.ylabel("Y")
print(x)
print(y)

plt.show() 
