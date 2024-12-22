/*14. Uso de propiedades 
Crea una clase Producto con propiedades Nombre, Precio y Cantidad. Calcula el total a 
pagar multiplicando el precio por la cantidad. Usa propiedades para validar que no se 
ingresen valores negativos. 
Temas: Propiedades, Clases.*/

using coreObjectOrientedConcepts;


namespace ejercicio13{
    class Program {
        static void Main(string[] args){
            Producto Huevo = new Producto();
            Huevo.CalcularValor();
            Producto Huevo2 = new Producto("Huevo AA", 30, 10000);
            Huevo2.CalcularValor();
            Producto Aguacate = new Producto("Aguacate", -2, 8000);
            Aguacate.CalcularValor();
        }
    }
}