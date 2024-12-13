using System;

class Program
{
    static void Main()
    {
        Console.WriteLine("Iniciando tareas sincrónicas...");

        // Tarea 1: Preparar el café
        PrepararCafe();

        // Tarea 2: Hacer tostadas
        HacerTostadas();

        Console.WriteLine("¡Todo listo!");
    }

    static void PrepararCafe()
    {
        Console.WriteLine("Preparando el café...");
        System.Threading.Thread.Sleep(3000); // Simula que tarda 3 segundos
        Console.WriteLine("Café listo.");
    }

    static void HacerTostadas()
    {
        Console.WriteLine("Haciendo las tostadas...");
        System.Threading.Thread.Sleep(2000); 
        Console.WriteLine("Tostadas listas.");
    }
}
