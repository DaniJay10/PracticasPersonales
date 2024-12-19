namespace coreObjectOrientedConcepts{
    class Programador : Persona {
        public string LenguajeFavorito;

        //Constructor defecto
        public Programador() : base(){
            LenguajeFavorito = "C#";
        }

        //Constructor con parametros
        public Programador(string Nombre, int Edad, string LenguajeFavorito) : base(Nombre,Edad){
            this.LenguajeFavorito = LenguajeFavorito;
        }

        public override void MostrarInformacion(){
            base.MostrarInformacion();
            Console.WriteLine($"Lenguaje Favorito: {LenguajeFavorito}");
        }


    }
}