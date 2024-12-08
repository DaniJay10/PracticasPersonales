namespace coreObjectOrientedConcepts
{
    public partial class Persona
    {
        public int Edad { get; set; }  // Declaración de la propiedad 'Edad'

        partial void MostrarEdad()
        {
            Console.WriteLine($"La edad es {Edad}");
        }
    }
}
