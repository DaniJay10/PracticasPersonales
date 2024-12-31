/*Clases de festividades*/
using coreObjectOrientedConcepts;

namespace SeAcaboEl2024{
    class Program {
        static void Main(string[] args){
            Navidad Navidad2024 = new Navidad("Navidad", "25/12/2024", 8);
            Navidad2024.LlegoLaHora();

            NewYear NewYear2024 = new NewYear("Año nuevo", "01/01/2025", "Pernil de cerdo");
            NewYear2024.LlegoLaHora();
        }
    }
}