namespace coreObjectOrientedConcepts {
    internal class Producto {
        public string Nombre { get; set; }

        private double cantidad;
        public double Cantidad {
            get { return cantidad; }
            set {
                if (value < 0) {
                    Console.WriteLine("Cantidad no puede ser negativa. Se establecerá en 0.");
                    cantidad = 0;
                } else {
                    cantidad = value;
                }
            }
        }

        private double precio;
        public double Precio {
            get { return precio; }
            set {
                if (value < 0) {
                    Console.WriteLine("Precio no puede ser negativo. Se establecerá en 0.");
                    precio = 0;
                } else {
                    precio = value;
                }
            }
        }

        public Producto() {
            Nombre = "";
            Cantidad = 0;
            Precio = 0;
        }

        public Producto(string nombre, double cantidad, double precio) {
            Nombre = nombre;
            Cantidad = cantidad; 
            Precio = precio;     
        }
        public void CalcularValor() {
            double precioFinal = Cantidad * Precio;
            Console.WriteLine($"El valor del producto '{Nombre}' es: {precioFinal}");
        }
    }
}
