namespace coreObjectOrientedConcepts {
    internal abstract class Festividad {
        public string Nombre;
        public string Fecha;

        //Constructor por defecto
        public Festividad(){
            Nombre = "Cumpleaños";
            Fecha = "18/12/2022";
        }

        //Constructor
        public Festividad(string Nombre, string Fecha){
            this.Nombre = Nombre;
            this.Fecha = Fecha;
        }

        public virtual void LlegoLaHora(){
            Console.WriteLine($"Estamos a {Fecha}, Ya es {Nombre}")
        }
    }
}