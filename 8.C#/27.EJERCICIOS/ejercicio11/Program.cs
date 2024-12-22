/*11.Uso de Enum 
Crea un enum llamado DiasSemana con los días de la semana. Solicita al usuario un número 
del 1 al 7 e imprime el día correspondiente. 
Temas: Enum, Condicionales.*/



namespace ejercicio11{
    class Program{
    enum DiasSemanas : int {
        Lunes,
        Martes,
        Miercoles,
        Jueves,
        Viernes,
        Sabado,
        Domingo
    }
        static void Main(string[] args){
            int dia = 0;
            Console.WriteLine("Ingrese numero dia de la semana");
            dia = int.Parse(Console.ReadLine());
            while ( dia > 7 || dia <= 0){
                Console.WriteLine("Error: Ingrese un dia valido (1-7)");
                dia = int.Parse(Console.ReadLine());
            }
            DiasSemanas diaSemana = (DiasSemanas)(dia - 1);
            Console.WriteLine($"El día de la semana es: {diaSemana}");


        
        }
    }
}