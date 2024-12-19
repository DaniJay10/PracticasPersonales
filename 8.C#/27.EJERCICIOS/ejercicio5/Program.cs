/*5.Búsqueda de palabras en una cadena 
Solicita al usuario una oración y una palabra. Busca cuántas veces aparece la palabra en la 
oración ingresada. 
Temas: Cadenas, Condicionales. */


using System;

namespace Buscador {
    class Program {
        static void Main(string[] args){
            string oracion = "";
            string palabra = "";
            Console.WriteLine("Ingrese una oracion");
            oracion = Console.ReadLine();
            Console.WriteLine("Ingrese una palabra");
            palabra = Console.ReadLine();

            int contador = 0;

            string [] partesOracion = oracion.Split(' ');
            foreach ( string parte in partesOracion){
                if(parte.ToLower() == palabra.ToLower()){
                    contador += 1;
                }
            }

            Console.WriteLine($"La palabra: {palabra} se repite: {contador} veces en la oracion");


        }
    }
}