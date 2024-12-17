/* 2.Calculadora básica 
Desarrolla una calculadora que permita realizar suma, resta, multiplicación y división entre 
dos números según la opción elegida por el usuario. 
Temas: Condicionales, Operadores, Métodos. */


using System;

namespace Calculadora
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 0;
            int b = 0;
            int controlador = 0;

            Console.WriteLine("Digite numero 1");
            a = int.Parse(Console.ReadLine());

            Console.WriteLine("Digite numero 2");
            b = int.Parse(Console.ReadLine());

            Console.WriteLine("Seleccione una Opcion:");
            Console.WriteLine("1. Suma");
            Console.WriteLine("2. Resta");
            Console.WriteLine("3. Multiplicacion");
            Console.WriteLine("4. Division");

            controlador = int.Parse(Console.ReadLine());

            switch (controlador)
            {
                case 1:
                    Console.WriteLine($"La suma de {a} y {b} es: {a + b}");
                    break;
                case 2:
                    Console.WriteLine($"La resta de {a} y {b} es: {a - b}");
                    break;
                case 3:
                    Console.WriteLine($"La multiplicacion de {a} y {b} es: {a * b}");
                    break;
                case 4:
                    if (b == 0){
                        Console.WriteLine("Error: No se puede dividir por 0");
                    }
                    else{
                        Console.WriteLine($"La division de {a} y {b} es: {a / b}");
                    }
                    break;
                default:
                    Console.WriteLine("Opcion no valida");
                    break;
            }
        }
    }
}
