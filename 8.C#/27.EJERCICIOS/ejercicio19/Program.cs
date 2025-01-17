using System;
using coreObjectOrientedConcepts;
namespace Hospital {
    class Program {
        public static void Main(string[] args){

            //Doctor
            Doctor internista = new Doctor("Marjorie Ortega", 60, 63245245, 1234242, "marjorie@gmail.com", "Internista");
            internista.DatosUsuario();

            //Paciente
            Paciente paciente1 = new Paciente("Daniel Jay", 21, 10052332, 233323, "daniel@gmail.com", "Gastritis");
            paciente1.DatosUsuario();

            //Cita
            Citas cita1 = new Citas();
            Console.WriteLine(cita1.Fecha);

            Citas cita2 = new Citas("16:45", "16/01/2025", internista, paciente1);
            Console.WriteLine("Doctor: " + cita2.Doctor.Nombre);
            Console.WriteLine("Paciente: " + cita2.Paciente.Nombre);
            Console.WriteLine("Fecha: " + cita2.Fecha);
            Console.WriteLine("Hora: " + cita2.Hora);

            Console.WriteLine("Hola");


        }
    }
}
