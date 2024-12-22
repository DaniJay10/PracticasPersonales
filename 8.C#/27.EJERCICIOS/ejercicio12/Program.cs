/*12.Delegado para operaciones matemáticas 
Define un delegado que realice operaciones matemáticas simples como suma, resta, 
multiplicación y división. Usa métodos para realizar cada operación e invoca el delegado. 
Temas: Delegate.*/


namespace ejercicio12 {
    delegate int Operacion(int num1, int num2); //Los delegados no se pueden definir en el MAIN
    class Program{
        static void Main(string[] args){
            Console.WriteLine("Suma, resta, multiplicacion y division de 10 y 5:");
            int Sumar(int num1, int num2) => num1 + num2;
            int Restar(int num1, int num2) => num1 - num2;
            int Multiplicar(int num1, int num2) => num1 * num2;
            int Dividir(int num1, int num2) => num1 / num2;
            Operacion operacion;
            operacion = Sumar;
            Console.WriteLine($"Suma: {operacion(10, 5)}");
            operacion = Restar;
            Console.WriteLine($"Resta: {operacion(10, 5)}");
            operacion = Multiplicar;
            Console.WriteLine($"Multiplicacion: {operacion(10, 5)}");
            operacion = Dividir;
            Console.WriteLine($"Division: {operacion(10, 5)}");
        }
    }
}