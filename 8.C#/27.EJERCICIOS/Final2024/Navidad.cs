namespace coreObjectOrientedConcepts {
    internal class Navidad : Festividad {
        public int Regalos;

        //Constructor sin parametros
        public Navidad() : base(){
            Regalos = 5;
        }

        //Constructor con parametros
        public Navidad(string Nombre, string Fecha, int Regalos) : base(Nombre, Fecha){
            this.Regalos = Regalos;
        }

        public override void LlegoLaHora(){
            base.LlegoLaHora();
            Console.WriteLine($"feliz navidad tararara");
            Console.WriteLine($"Recibi {Regalos} Regalos");
        }

    }
}