using ConceptosBasicos;

Codigo codigo = new Codigo();

// Asignar un método anónimo al delegado
Codigo.DelegadoMensaje mensaje = delegate
{
    Console.WriteLine("¡Este es un método anónimo!");
};

// Llamar al método que ejecuta el delegado
codigo.EjecutarMetodo(mensaje);

Console.ReadLine();

