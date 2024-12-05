/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package CentroSalud;
import java.util.ArrayList;
/**
 *
 * @author Estudiante
 */
public class Paciente extends Persona{
    private int estrato;
    private String ciudad="GironCity";
    public ArrayList<Cita> citas = new ArrayList<Cita>(); 
    
    public Paciente(int nif, String nombre,int año, int month, int day,int estrato, String ciudad){
       super(nif,nombre,año,month,day);
       this.estrato=estrato;
       this.ciudad=ciudad;
    }
   public Paciente(int nif, String nombre,int estrato, String ciudad){
   super(nif,nombre);
   this.estrato=estrato;
   this.ciudad=ciudad;
   }
    
    
    //añadir cita
    public void añadirCita(Cita c){
    this.citas.add(c);
    }
    
    public int getEstrato() {
        return estrato;
    }

    public void setEstrato(int estrato) {
        this.estrato = estrato;
    }

   
    
}
