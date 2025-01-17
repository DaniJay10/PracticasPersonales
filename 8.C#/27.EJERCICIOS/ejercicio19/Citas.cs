namespace coreObjectOrientedConcepts {
    internal class Citas {
        public string Hora;
        public string Fecha;
        public Doctor Doctor;
        public Paciente Paciente;
        //Constructor por defecto
        public Citas(){
            Hora = "NA";
            Fecha = "NA";
            Doctor = new Doctor();
            Paciente = new Paciente();
        }
        //Constructor con parametros
        public Citas(string Hora, string Fecha, Doctor Doctor, Paciente Paciente){
            this.Hora = Hora;
            this.Fecha = Fecha;
            this.Doctor = Doctor;
            this.Paciente = Paciente;
        }
    }
}