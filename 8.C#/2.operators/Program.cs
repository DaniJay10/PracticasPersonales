int salario = 1300000;
float cesantias = 8.33f;
int pension = 16;

float salarioFinal = salario - (salario*cesantias/100) - (salario*pension/100);

Console.WriteLine($"El salario final es: ${salarioFinal}");

//ejercicio 2
int temperatura = 50;
if(temperatura >  60)
    Console.WriteLine("Hace mucho calor.");
else
    Console.WriteLine("Hace mucho frio.");

//ejercicio 3
bool CorreoCorrecto = true;
bool ContraCorrecta = true;
bool usuarioCorrecto = false;

if(CorreoCorrecto&&usuarioCorrecto&&ContraCorrecta)
    Console.WriteLine("Usuario logueado correctamente.");
else
    Console.WriteLine("Usuario o contraseña incorrectos.");