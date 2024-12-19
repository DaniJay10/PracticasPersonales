/*Crea una clase Rectangulo con propiedades: Base y Altura. Añade un método para calcular el 
área y otro para el perímetro. Crea varios objetos y muestra sus valores. 
Temas: Clases, Métodos.*/

using coreObjectOrientedConcepts;

namespace ejercicio8{
    class Program{
        static void Main(string[] args){
            //rectangulo 1 sin parametros
            Rectangulo rect1 = new Rectangulo();
            rect1.CalcularArea();
            rect1.CalcularPerimetro();

            //rectangulo con parametros
            Rectangulo rect2 = new Rectangulo(3, 4);
            rect2.CalcularArea();
            rect2.CalcularPerimetro();
        }
    }
}