namespace coreObjectOrientedConcepts{
    internal class Calculation{
        public void calculate(int x, int y){
          try{
               int result = x/y;
              Console.WriteLine($"La division de {x} y {y} es {result}");
          }
          catch(Exception ex){ //El Exception ex maneja todas las excepciones y solo con un bloque basta
               Console.WriteLine($"Ha ocurrido un error");
               Console.WriteLine($"Error: {ex.Message}");
          }
          finally{
              Console.WriteLine("Este bloque se ejecuta siempre");
          }
        }

        public void calculateAnother(){
            try{
                int a, b, result = 0;
                Console.WriteLine("Ingrese el primer número:");
                a = int.Parse(Console.ReadLine());
                Console.WriteLine("Ingrese el segundo número:");
                b = int.Parse(Console.ReadLine());
                result = a / b;
                Console.WriteLine($"La division de {a} y {b} es {result}");
            }
            catch(DivideByZeroException ex){
               Console.WriteLine($"Error: Division por cero");
            }
            catch(FormatException ex){
               Console.WriteLine($"Error: Dato no numerico ingresado.");
            }
            catch(Exception ex){
               Console.WriteLine($"Ha ocurrido un error");
               Console.WriteLine($"Error: {ex.Message}");
            }
            finally{
              Console.WriteLine("Este bloque se ejecuta siempre");
          }
        }
    }
}