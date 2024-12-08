namespace coreObjectOrientedConcepts
{
    public partial class Persona
    {
        public string Nombre { get; set; }
        public string Apellido { get; set; }

        public void MostrarInformacion()
        {
            MostrarEdad(); // Llamada al método parcial
        }

        partial void MostrarEdad();
    }
}
