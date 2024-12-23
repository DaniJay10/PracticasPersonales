using System;
using System.Collections.Generic;

namespace FiltrarNumerosImpares
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> numeros = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

            List<int> numerosImpares = numeros.FindAll(delegate (int n) {
                return n % 2 != 0; 
            });
            Console.WriteLine("Números impares:");
            foreach (int impar in numerosImpares)
            {
                Console.WriteLine(impar);
            }
        }
    }
}
