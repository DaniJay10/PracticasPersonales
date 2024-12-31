namespace coreObjectOrientedConcepts{
    class NewYear : Festividad{
        public string Cena;

        public NewYear() : base(){
            Cena = "Cerdo";
        }

        public NewYear(string Nombre, string Fecha, string Cena) : base(Nombre, Fecha){
            this.Cena = Cena;
        }

        public override void LlegoLaHora(){
            base.LlegoLaHora();
            Console.WriteLine($"Año nuevo vida nueva");
            Console.WriteLine($"Primo se te esta quemando el {Cena} :v");
        }
        
     }
}