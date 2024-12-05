/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package CentroSalud;

import java.util.Scanner;

/**
 *
 * @author Estudiante
 */
public class Prueba {
    public static void main(String[] args) {
      Scanner entrada = new Scanner(System.in);
      
    
      
      
      
      Paciente paciente1 = new Paciente(1, "Yeimy","Calle 3",316,'F',4,"Pedro",2000,1,1);
      System.out.println(paciente1.getDireccion());
      paciente1.setDireccion("calle 4 #5");
      System.out.println(paciente1.getDireccion());
      Medico medico = new Medico (1, "Yeimy","Calle 3",316,'F',
              "Odontologia","General","San Andres","08:00am/06:00pm",2000,1,1);
      System.out.println(medico.getHorario());
      
    }
}
