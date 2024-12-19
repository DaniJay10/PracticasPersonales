namespace coreObjectOrientedConcepts {
    class Ingeniero : Persona{
        public string Especialidad;

        //Constructor base
        public Ingeniero() : base(){
            Especialidad = "Telecomunicaciones";
        }

        public Ingeniero(string Nombre, int Edad, string Especialidad) : base(Nombre, Edad){
            this.Especialidad = Especialidad;

        }


        public override void MostrarInformacion(){
            base.MostrarInformacion();
            Console.WriteLine($"Especialidad: {Especialidad}");
        }
    }
}