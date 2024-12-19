/*Crea una interfaz IFigura con un método CalcularArea. 
Implementa esta interfaz en las clases Cuadrado y Triangulo. Crea objetos de ambas clases y 
calcula el área. 
Temas: Interfaces, POO.*/

using coreObjectOrientedConcepts;

namespace interfacesFiguras{
    class Program {
        static void Main(string[] args) {
            Console.WriteLine("Sin parametros");
            Cuadrado cuadrado = new Cuadrado();
            cuadrado.CalcularArea();
            Triangulo triangulo = new Triangulo();
            triangulo.CalcularArea();
            Console.WriteLine("Con parametros");
            Cuadrado cuadrado2 = new Cuadrado(8);
            cuadrado2.CalcularArea();
            Triangulo triangulo2 = new Triangulo(8, 8);
            triangulo2.CalcularArea();
    }
  }
}