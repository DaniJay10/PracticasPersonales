using System;
/*17. Ejercicio de Lambda 
Ordenar nombres con expresiones Lambda 
Crea una lista de nombres (ejemplo: "Ana", "Pedro", "Luis", "Carlos"). 
Utiliza una expresión Lambda con List<T>.Sort() para ordenar los nombres en orden 
alfabético inverso (de Z a A). 
Muestra la lista ordenada. 
Temas: Lambda Expressions, Listas. */

namespace Ejercicio17{
    class Program{
        static void Main(string[] args){
            List<string> nombres = new List<string>{"Ana", "Pedro", "Luis", "Carlos"};
            nombres.Sort((a, b) => b.CompareTo(a));
            foreach(string n in nombres){
                Console.WriteLine(n);
            }
        }
    }
}
