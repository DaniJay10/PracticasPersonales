/*3.Tabla de multiplicar 
Pide un número al usuario y muestra la tabla de multiplicar del 1 al 10 usando un bucle. 
Temas: Bucles, Condicionales.*/


using System;

namespace TablasMultiplicar {
    class Program {
        static void Main(string[] args){
            int numero = 0;
            while(numero < 1){
                Console.WriteLine("Ingrese numero que desea ver la tabla de multiplicar");
                numero = int.Parse(Console.ReadLine());
                if(numero < 1){
                    Console.WriteLine("Error: Ingrese un numero mayor a cero");
                }
            }

            for (int i = 1; i<=10; i++){
                Console.WriteLine($"{numero} * {i} = {numero*i}");
            }
        }
    }
}