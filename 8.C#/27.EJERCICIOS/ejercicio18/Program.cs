/*18. Ejercicio de Expression Trees 
Construir una operación matemática simple con Expression Trees 
Usa System.Linq.Expressions para crear un árbol de expresión que represente la operación 
matemática: x + y. 
Compila la expresión y ejecútala para valores x = 5 e y = 3. Muestra el resultado. 
Temas: Expression Trees, Expresiones dinámicas.*/
using System.Linq.Expressions;
using System.Numerics;

Expression<Func<int, int, int>> Sumar = (a, b) => a+b;

var ejecucion = Sumar.Compile();
int resultado = ejecucion(5, 3);
Console.WriteLine(resultado); 
