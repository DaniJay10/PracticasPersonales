using ConceptosBasicos;

Numero numero = new Numero();


numero.EventoNumeroImpar += MensajeImpar;

// Pedir al usuario un número
Console.WriteLine("Ingresa un número:");
int num = int.Parse(Console.ReadLine());

// Verificar el número
numero.VerificarNumero(num);

Console.ReadLine();


static void MensajeImpar()
{
    Console.WriteLine("¡Se detectó un número impar!");
}
