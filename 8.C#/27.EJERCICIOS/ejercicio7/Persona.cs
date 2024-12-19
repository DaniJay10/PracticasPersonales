namespace coreObjectOrientedConcepts {
    internal abstract class Persona {
        public string Nombre;
        public int Edad;

        //Constructor default
        public Persona(){
            Nombre = "NA";
            Edad = 0;
        }

        public Persona(string Nombre, int Edad){
            this.Nombre = Nombre;
            this.Edad = Edad;
        }

        public virtual void MostrarInformacion(){
            Console.WriteLine($"Nombre: {Nombre}");
            Console.WriteLine($"Edad: {Edad}");
        }
    }
}