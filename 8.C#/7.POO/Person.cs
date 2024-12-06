namespace coreObjectOrientedConcepts {
    internal abstract class Person {
        protected string name;

        //constructor default
        public Person(){
            name = "Uknown";
        }

        //Constructor con parametros
        public Person(string name){
            this.name = name;
        }

        public virtual void displayDetails(){ //El virtual permitira sobreescribirlo en una clase hija
            Console.WriteLine($"Name: {name}");
        }
    }
}