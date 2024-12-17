/*4.Promedio de calificaciones 
Crea un programa que permita ingresar las calificaciones de 5 estudiantes y calcule el 
promedio de las mismas. 
Temas: Arrays, Bucles.*/

using System.Text;
using System;
namespace promedioNota {
    class Program {
        static void Main(string[] args){

            int[] notas = new int[5];

            for(int i=0; i < 5; i++){
                Console.WriteLine($"Ingrese nota del estudiante {i+1}");
                notas[i] = int.Parse(Console.ReadLine());
            }
            Console.WriteLine("Notas:");
            int acumulador = 0;
            for(int i=0 ; i < notas.Length; i++){
                Console.WriteLine($"Estudiante {i+1}: {notas[i]}");
                acumulador += notas[i];
            }

            int promedio = acumulador/notas.Length;
            Console.WriteLine($"El promedio de las notas es: {promedio}");

        }
    }
}

