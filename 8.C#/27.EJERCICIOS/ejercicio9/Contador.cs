namespace coreObjectOrientedConcepts {
    class Contador {
        public static int Numeroinstancias = 0;

        public Contador(){
            Numeroinstancias++;
        }

        public static void VerNumeroInstancias(){
            Console.WriteLine($"Número de instancias de la clase contador: {Numeroinstancias}");
        }
    }
}