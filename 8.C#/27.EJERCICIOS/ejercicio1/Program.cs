/*1.Suma de números pares 
Escribe un programa que solicite un número entero positivo n y sume todos los números 
pares del 1 hasta n usando un bucle for. 
Temas: Condicionales, Bucles, Operadores. 
*/

using System;

int numero = 0;
int suma = 0;
while(numero < 1){
    Console.WriteLine("Ingrese un numero positivo");
    numero = int.Parse(Console.ReadLine());
    if(numero < 0 || numero == 0){
        Console.WriteLine("Error: Ingrese un numero mayor a cero");
    }
}
Console.WriteLine($"El numero es: {numero}");

for(int i=1; i <= numero; i++){
    if(i % 2 == 0){
        suma += i;
    }
}
Console.WriteLine($"suma de pares de 1 a {numero} es: {suma}");


