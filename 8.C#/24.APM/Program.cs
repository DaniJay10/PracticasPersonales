using System;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        Console.WriteLine("Iniciando operación de suma asíncrona...");

        // Ejecutamos la suma de manera asíncrona usando Task
        Task<int> tareaSuma = Task.Run(() => Sumar(5, 3));

        Console.WriteLine("Haciendo otras cosas mientras se realiza la suma...");

        // Esperamos el resultado de la tarea
        int resultado = await tareaSuma;

        Console.WriteLine($"La suma ha terminado. Resultado: {resultado}");
    }

    // Método que realiza la suma
    static int Sumar(int a, int b)
    {
        return a + b;
    }
}
