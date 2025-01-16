namespace coreObjectOrientedConcepts {
    internal class Paciente : Persona {
        public string Diagnostico;
        //Constructor por defecto
        public Paciente() : base() {
            Diagnostico = "No aplica";
        }
        
        //Constructor con parametros
        public Paciente(string Nombre, int Edad, int Cedula, int Telefono, string Correo, string Diagnostico) : base(Nombre, Edad, Cedula, Telefono, Correo) {
            this.Diagnostico = Diagnostico;
        }

        public override void DatosUsuario(){
            base.DatosUsuario();
            Console.WriteLine($"Diagnostico: {Diagnostico}");
        }
    }
}