var persona = new { Nombre = "Daniel", 
Edad = 21,
Direccion = new {calle = "52 #16-70", barrio = "San Miguel"},
Proyectos = new[]{
    new {Proyecto = "React", DuracionHoras = 40},
    new {Proyecto = "Angular", DuracionHoras = 35},
    new {Proyecto = "Vue.js", DuracionHoras = 25}
}};




Console.WriteLine($"Nombre: {persona.Nombre}, Edad: {persona.Edad}, Direccion: {persona.Direccion.calle} {persona.Direccion.barrio}");
Console.WriteLine("Proyectos:");
foreach(var project in persona.Proyectos){
    Console.WriteLine($"Proyecto: {project.Proyecto}, Duracion Horas: {project.DuracionHoras}");
}
//Se podria decir que Anonymous Type es la manera de crear objetos sin necesidad de crear una clase

