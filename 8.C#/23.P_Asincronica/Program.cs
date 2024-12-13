using System;
using System.Threading.Tasks;

class Program {
    static async Task Main(){
        Console.WriteLine("Iniciando tareas asincrónicas...");
        // Iniciamos ambas tareas asincrónicamente
        Task tareaCafe = PrepararCafe();
        Task tareaTostadas = HacerTostadas();
        
        await Task.WhenAll(tareaCafe, tareaTostadas);

        Console.WriteLine("¡Todo listo!");
    }
    static async Task PrepararCafe()
    {
        Console.WriteLine("Preparando el café...");
        await Task.Delay(3000); 
        Console.WriteLine("Café listo.");
    }
    static async Task HacerTostadas()
    {
        Console.WriteLine("Haciendo las tostadas...");
        await Task.Delay(2000); 
        Console.WriteLine("Tostadas listas.");
    }

}