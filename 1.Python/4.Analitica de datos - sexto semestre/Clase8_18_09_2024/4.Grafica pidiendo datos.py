import matplotlib.pyplot as plt
valor1=int(input("Digite valor inicio x"))
valor2=int(input("Digite valor fin x"))
y=[]
x=range(valor1,valor2,1)
for i in x:
    y.append(i**2)

plt.plot(x,y)
plt.title("FUNCION PARABOLICA")
plt.xlabel("X")
plt.ylabel("Y")
print(x)
print(y)

plt.show() 