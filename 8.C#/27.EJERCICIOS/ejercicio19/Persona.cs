namespace coreObjectOrientedConcepts {
    internal abstract class Persona {
        public string Nombre;
        public int Edad;
        public int Cedula;
        public int Telefono;
        public string Correo;

        //Constructor default 
        public Persona(){
            Nombre = "NA";
            Edad = 0;
            Cedula = 0;
            Telefono = 0;
            Correo = "NA";
        }
        //Constructor con parametros
        public Persona(string Nombre, int Edad, int Cedula, int Telefono, string Correo){
            this.Nombre = Nombre;
            this.Edad = Edad;
            this.Cedula = Cedula;
            this.Telefono = Telefono;
            this.Correo = Correo;
        }

        public virtual void DatosUsuario(){
            Console.WriteLine($"Nombre: {Nombre}");
            Console.WriteLine($"Edad: {Edad}");
            Console.WriteLine($"Cedula: {Cedula}");
            Console.WriteLine($"Telefono: {Telefono}");
            Console.WriteLine($"Correo: {Correo}");
        }
    }
}