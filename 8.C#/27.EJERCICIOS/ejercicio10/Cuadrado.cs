namespace coreObjectOrientedConcepts {
    internal class Cuadrado : Figura {
        public float lado;

        public Cuadrado(){
            lado = 4;
        }

        public Cuadrado(float lado){
            this.lado = lado;
        }

        public void CalcularArea(){
            float Area = lado * lado;
            Console.WriteLine($"El área del cuadrado es: {Area}");
        }
    }
}