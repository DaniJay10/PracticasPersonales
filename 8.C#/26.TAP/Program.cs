using System;
using System.Threading.Tasks;

class Program
{
    // Método asincrónico básico
    static async Task MostrarMensajeAsync()
    {
        Console.WriteLine("Iniciando la tarea...");

        // Simula una operación que tarda 3 segundos (por ejemplo, cargar algo)
        await Task.Delay(3000);

        Console.WriteLine("¡Tarea completada! El mensaje se ha mostrado.");
    }

    // Método principal
    static async Task Main(string[] args)
    {
        Console.WriteLine("Programa iniciado.");
        
        // Llama al método asincrónico
        await MostrarMensajeAsync();

        Console.WriteLine("Programa finalizado.");
    }
}
