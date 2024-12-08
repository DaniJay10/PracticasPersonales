using coreObjectOrientedConcepts;

class Program
{
    static void Main()
    {
        Persona persona = new Persona
        {
            Nombre = "Juan",
            Apellido = "Pérez",
            Edad = 30
        };

        persona.MostrarInformacion(); 
    }
}
