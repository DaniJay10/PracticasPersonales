import random

caracteres = "0123456789zxcvbnmasdfghjklqwertyuiop+*-/#&%$!"

def crear(longitud):
    a = ""
    for i in range(longitud):
        a += random.choice(caracteres)
    return a

