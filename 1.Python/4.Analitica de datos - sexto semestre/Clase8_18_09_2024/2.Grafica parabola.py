import matplotlib.pyplot as plt
y=[]
x=range(-5,6,1)
for i in x:
    y.append(i**2)

plt.plot(x,y)
plt.title("FUNCION PARABOLICA")
plt.xlabel("X")
plt.ylabel("Y")
print(x)
print(y)

plt.show() 
