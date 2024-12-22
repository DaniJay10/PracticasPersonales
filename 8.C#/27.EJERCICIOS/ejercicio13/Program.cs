/*13.Evento de alarma 
Crea una clase Alarma con un evento OnAlarmaActivada. Este evento debe activarse cuando 
se cumpla una condición, como que una temperatura exceda un límite. 
Temas: Eventos, Delegate. */

using coreObjectOrientedConcepts;

namespace AlarmaEventos{
    class Program{
        static void Main(string[] args){
            Alarma LASOPA = new Alarma();
            LASOPA.OnAlarmaActivada += MensajeAlarma;
            Console.WriteLine("Ingrese temperatura actual");
            float temp = float.Parse(Console.ReadLine());
            LASOPA.VerificarAlarma(temp);
            static void MensajeAlarma(){
                Console.WriteLine("ALARMA ACTIVADA! TEMPERATURA EXCEDIDA!");
            }
}}}