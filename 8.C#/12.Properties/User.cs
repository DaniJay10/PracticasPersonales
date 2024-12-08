namespace coreObjectOrientedConcepts{
    internal class User{
        private string name;
        private string email;
        public User() {
            email = "danielpinzon@gmail.com";
        }
        public string Name {
            set {name = value;}
            get {return name;}
        }
        public string Email {
            get { return email;}
        }
    }
}