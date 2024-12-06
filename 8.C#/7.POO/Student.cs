namespace coreObjectOrientedConcepts {
    internal class Student : Person{
        private int studentID;
        private string grado;
        
        // defaultConstructor
        public Student() : base() { // Llama al constructor por defecto de la clase base
            studentID = 100;
            grado = "8A";
        }
        
        //Constructor con parametros
          public Student(int id, string name, string grado) : base(name) { // Llama al constructor con parámetros de la clase base
            studentID = id;
            this.grado = grado; // Usa 'this' para referirse al atributo
        }

        //Metodos

        //Recopilar detalles
        /*public void acceptDetails(){
            Console.WriteLine("Ingrese ID");
            studentID = int.Parse(Console.ReadLine());
            Console.WriteLine("Ingrese nombre");
            studentName = Console.ReadLine();
    
        }*/
        public override void displayDetails() {
            base.displayDetails(); // Llama al método displayDetails de la clase base
            Console.WriteLine($"Student ID: {studentID}, Grado: {grado}");
        }
    }
}