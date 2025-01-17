namespace coreObjectOrientedConcepts {
    internal class Doctor : Persona {
        public string Especialidad;

        //Constructor base
        public Doctor() : base() {
            Especialidad = "General";
        }

        //Constructor con parametros
        public Doctor(string Nombre, int Edad, int Cedula, int Telefono, string Correo, string Especialidad) : base(Nombre, Edad, Cedula, Telefono, Correo){
            this.Especialidad = Especialidad;
        }

        public override void DatosUsuario(){
            base.DatosUsuario();
            Console.WriteLine($"Especialidad: {Especialidad}");
        }

    }
}