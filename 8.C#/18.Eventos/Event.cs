namespace ConceptosBasicos
{
    internal class Numero
    {
        // Declarar el delegado
        public delegate void DelegadoNumero();

        // Declarar el evento basado en el delegado
        public event DelegadoNumero EventoNumeroImpar;

        // Método que verifica si un número es par o impar
        public void VerificarNumero(int numero)
        {
            Console.WriteLine($"Número ingresado: {numero}");
            if (numero % 2 != 0) // Si el número es impar
            {
                EventoNumeroImpar?.Invoke(); // Disparar el evento si hay suscriptores
            }
        }
    }
}
