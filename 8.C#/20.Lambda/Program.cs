using System;

public delegate void MiDelegado(string mensaje);

class Program
{
    static void Main(string[] args)
    {
        MiDelegado mostrarMensaje = (mensaje) => {
            Console.WriteLine($"El mensaje es: {mensaje}");
        };

        mostrarMensaje("¡Hola desde una expresión lambda!");

        Console.ReadLine();
    }
}
