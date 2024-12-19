namespace coreObjectOrientedConcepts{
    class Rectangulo{
        public float Base;
        public float Altura;

        public Rectangulo(){
            Base = 1.01f;
            Altura = 1.05f;
        }

        public Rectangulo(float Base, float altura){
            this.Base = Base;
            this.Altura = altura;
        }

        public void CalcularArea(){
            float Area = Base * Altura;
            Console.WriteLine($"El área del rectángulo es: {Area}"); 
        }

        public void CalcularPerimetro(){
            float Perimetro = 2 * (Base + Altura);
            Console.WriteLine($"El Perimetro del rectangulo es: {Perimetro}");
        }
    }
}