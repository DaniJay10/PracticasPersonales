/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package CentroSalud;



/**
 *
 * @author Estudiante
 */
public class Prueba {
    public static void main(String[] args) {
      Medico Paco = new Medico(6,"Paco","General","Pediatra",1200000);
      Paciente Daniel = new Paciente(1,"Daniel",4,"Bucaramanga");
      Cita cita1= new Cita(Paco,Daniel,"19/08/2023","4:30 pm","General",2);
      Paco.añadirCita(cita1);
      Daniel.añadirCita(cita1);
     System.out.println(Paco.citas.size());
     System.out.println(Daniel.citas.get(0).medico);
      

      
    }
}
