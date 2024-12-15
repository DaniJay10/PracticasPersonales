using System;
using System.ComponentModel; // Necesario para el patrón EAP
using System.Threading;

class Descargador
{
    // Evento que notifica cuando la descarga se completa
    public event EventHandler<AsyncCompletedEventArgs> DescargaCompletada;

    // Evento que notifica el progreso de la descarga
    public event ProgressChangedEventHandler ProgresoCambiado;

    // Método asíncrono para iniciar la descarga
    public void DescargarArchivoAsync()
    {
        BackgroundWorker worker = new BackgroundWorker();

        // Configuramos el trabajador para informar progreso
        worker.WorkerReportsProgress = true;

        // Configuramos el evento de progreso
        worker.ProgressChanged += (s, e) =>
        {
            ProgresoCambiado?.Invoke(this, e);
        };

        // Configuramos la tarea que realiza la "descarga"
        worker.DoWork += (s, e) =>
        {
            for (int i = 1; i <= 100; i += 10)
            {
                Thread.Sleep(200); // Simulamos trabajo
                worker.ReportProgress(i);
            }
        };

        // Configuramos la finalización
        worker.RunWorkerCompleted += (s, e) =>
        {
            DescargaCompletada?.Invoke(this, new AsyncCompletedEventArgs(null, false, null));
        };

        // Iniciamos la descarga
        worker.RunWorkerAsync();
    }
}

class Program
{
    static void Main()
    {
        Descargador descargador = new Descargador();

        // Suscribimos a los eventos
        descargador.ProgresoCambiado += (s, e) =>
        {
            Console.WriteLine($"Progreso: {e.ProgressPercentage}%");
        };

        descargador.DescargaCompletada += (s, e) =>
        {
            Console.WriteLine("¡Descarga completada!");
        };

        // Iniciamos la descarga
        Console.WriteLine("Iniciando descarga...");
        descargador.DescargarArchivoAsync();

        Console.WriteLine("Presiona ENTER para salir.");
        Console.ReadLine();
    }
}
