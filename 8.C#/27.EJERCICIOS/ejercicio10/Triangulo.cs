namespace coreObjectOrientedConcepts {
    internal class Triangulo : Figura {
        public float Base;
        public float Altura;

        public Triangulo(){
            Base = 4;
            Altura = 4;
        }

        public Triangulo(float Base, float Altura){
            this.Base = Base;
            this.Altura = Altura;
        }

        public void CalcularArea(){
            float Area = (Base * Altura) / 2;
            Console.WriteLine($"El área del triangulo es: {Area}");
        }
    }
}