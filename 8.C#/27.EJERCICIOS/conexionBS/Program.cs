using System;
using System.Data.SqlClient;

class Program
{
    static void Main()
    {
        // Cadena de conexión (ajusta con tus datos)
        string connectionString = "Server=localhost;Database=cchar;User Id=root;Password=spike10;";


        string nombre = "Carlos Pérez";
        int edad = 30;


        string insertQuery = "INSERT INTO Usuarios (Nombre, Edad) VALUES (@Nombre, @Edad)";

        try
        {
 
            using (SqlConnection connection = new SqlConnection(connectionString))
            {

                connection.Open();
                Console.WriteLine("Conexión establecida.");


                using (SqlCommand command = new SqlCommand(insertQuery, connection))
                {

                    command.Parameters.AddWithValue("@Nombre", nombre);
                    command.Parameters.AddWithValue("@Edad", edad);


                    int filasAfectadas = command.ExecuteNonQuery();

                    Console.WriteLine($"{filasAfectadas} registro(s) insertado(s) correctamente.");
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
