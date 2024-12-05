bool isAuthenticated = false;

//If
if (isAuthenticated)
Console.WriteLine("Bienvenido al sistema");
else
Console.WriteLine("Logeo incorrecto");

//Ternario
string message = isAuthenticated ? "Bienvenido al sistema" : "Logeo incorrecto (ternario)";
Console.WriteLine(message);

//Switch
string usuario = "admin";
switch(usuario)
{
    case "admin":
       Console.WriteLine("Es admin");
       break;
    case "usuarioNormal":
       Console.WriteLine("Es usuario");
       break;
    default:
       Console.WriteLine("Usuario no válido");
       break;
}