using System.Linq.Expressions;
using System.Numerics;


//Declarar la funcion lambda normal
Func<string, string, string> stringJoins = (str1, str2) => string.Concat(str1, str2);
//Aquí se declara una función lambda normal, que recibe dos cadenas (str1 y str2) y las concatena.

//Definicion del arbol de expresiones
Expression<Func<string, string, string>> stringJoinExpr = (str1, str2) => string.Concat(str1, str2);
//La diferencia clave aquí es que Expression<Func<>> no se ejecuta directamente
//En su lugar, almacena una representación en memoria de la operación que define.

//Metodo 1 de ejecucion
var func = stringJoinExpr.Compile();
var result = func("Hello", "World");
Console.WriteLine(result);

//Metodo 2 de ejecucion
result = stringJoinExpr.Compile()("Hello", "Everyone");
Console.WriteLine(result);

//Ejercicio: crea un arbol de expresiones que multiplique dos numeros:

Expression<Func<int, int, int>> multiplicar = (a,b) => a*b;
//Se tiene que poner 3 int debido a que el primero corresponde al dato 1, el segundo corresponde al dato 2 y el tercero al dato de salida
var ejecucion = multiplicar.Compile();
var resultado = ejecucion(4, 4);
Console.WriteLine(resultado);

//Ejercicio: crea un arbol de expresiones que calcule la raiz cuadrada de un numero:
Expression<Func<double, double>> raizCuadrada = (a) => Math.Sqrt(a);
var ejecucionR = raizCuadrada.Compile();
var resultado2 = ejecucionR(25);
Console.WriteLine(resultado2);