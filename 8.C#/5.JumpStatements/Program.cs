//BREAK
for(int i=0; i<=10; i++){
    if(i == 5) break;
    Console.WriteLine($"Hola mundo {i}");
}
Console.WriteLine("-------------------------------------------------------------");
//CONTINUE
for(int i=0; i<=10; i++){
    if(i == 5) continue; //NO APARECERA EL  HOLA MUNDO 5
    Console.WriteLine($"Hola mundo {i}");
}
//GOTO
string usuario = "admin";
switch(usuario)
{
    case "admin":
       Console.WriteLine("Es admin");
       goto case "usuarioNormal";
    case "usuarioNormal":
       Console.WriteLine("Es usuario");
       break;
    default:
       Console.WriteLine("Usuario no válido");
       break;
}
// RETURN
int Sumar(int a, int b)
{
    return a + b; 
}

Console.WriteLine($"La suma de 3 y 5 es: {Sumar(3, 5)}");

// THROW
int numero = -5;

if (numero < 0)
{
    throw new Exception("El número no puede ser negativo."); 
}

Console.WriteLine("El número es válido.");