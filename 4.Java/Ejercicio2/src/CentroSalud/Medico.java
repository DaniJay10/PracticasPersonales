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
public class Medico extends Persona{
    public String TipoMedico;
    public String especialidad;
    private int sueldo;
    public ArrayList<Cita> citas = new ArrayList<Cita>();
    public Medico(int nif, String nombre, String tipo, String esp, int sueldo){
    super(nif,nombre);
    this.TipoMedico=tipo;
    this.especialidad=esp;
    this.sueldo=sueldo;
    }
   public int calcularSueldo(){
   int pago = this.sueldo*12;
   return pago;
   }
   public void añadirCita(Cita c){
   this.citas.add(c);
   }
}
