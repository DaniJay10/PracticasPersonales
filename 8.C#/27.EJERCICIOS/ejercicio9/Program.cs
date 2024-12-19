/*Crea una clase Contador que tenga un atributo estático para contar cuántos objetos han sido 
creados de esa clase. */

using coreObjectOrientedConcepts;

namespace ejercicio9{
    class Program{
        static void Main(string[] args){
            Contador contador = new Contador();
            Contador contador2 = new Contador();
            Contador contador3 = new Contador();
            Contador contador4 = new Contador();
            Contador contador5 = new Contador();
            Contador.VerNumeroInstancias();
            //Recordar que los atributos estaticos son de la clase y no del objeto
         }
     }
}