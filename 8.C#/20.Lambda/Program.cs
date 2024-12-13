//Expression lambda
Func<int, int> square = x => x * x; 
Console.WriteLine(square(5)); // Salida: 25



//Statement lambda
Func<int, int> factorial = n =>
{
    int result = 1;
    for (int i = 1; i <= n; i++)
        result *= i;
    return result;
};
Console.WriteLine(factorial(5)); // Salida: 120
