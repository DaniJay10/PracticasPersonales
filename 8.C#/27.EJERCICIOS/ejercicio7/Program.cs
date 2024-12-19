/*Crea una clase Persona con propiedades: Nombre, Edad y un método MostrarDatos(). 
Crea una clase Programador que herede de Persona y añada una propiedad LenguajeFavorito. 
Crea un objeto de Programador y muestra los datos.Luego de esto cree otra clase que hereda
a persona a gusto.
Temas: POO, Herencia.*/

using coreObjectOrientedConcepts;
namespace ejercicio7{
    class Program{
        static void Main(string[] args){
            //Prorgamador
            Console.WriteLine("Programador con constructor sin parametros:");
            Programador David = new Programador();
            David.MostrarInformacion();
            Console.WriteLine("Programador con constructor con parametros:");
            Programador Daniel = new Programador("Daniel", 21, "Java");
            Daniel.MostrarInformacion();

            //Ingeniero
            Console.WriteLine("Ingeniero con constructor sin  parametros:");
            Ingeniero Yeimy = new Ingeniero();
            Yeimy.MostrarInformacion();
            Console.WriteLine("Ingeniero con constructor con parametros");
            Ingeniero Yuliana = new Ingeniero("Yuliana", 26, "Programacion");
            Yuliana.MostrarInformacion();
        }
    }
}