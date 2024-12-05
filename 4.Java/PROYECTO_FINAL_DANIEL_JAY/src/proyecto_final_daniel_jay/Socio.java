/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto_final_daniel_jay;

import java.util.ArrayList;

/**
 *
 * @author Estudiante
 */
public class Socio extends Persona{
    private String FechaIngreso;
    private ArrayList<Embarcaciones> Embarcaciones = new ArrayList<Embarcaciones>();
    private ArrayList<Puertos> Puertos = new ArrayList<Puertos>();
    
    
    //constructor socio sin puertos
    public Socio(String Nombre, int Cedula, String Direccion,int Telefono, int DiaNac, 
    int MesNac, int AñoNac,String FecIng,ArrayList<Embarcaciones> Embarcaciones){
    super(Nombre,Cedula,Direccion,Telefono,DiaNac,MesNac,AñoNac);
    this.FechaIngreso=FecIng;
    this.Embarcaciones=new ArrayList <>(Embarcaciones);
    }
    //constructor socio con puertos
    public Socio(String Nombre, int Cedula, String Direccion,int Telefono, int DiaNac, 
    int MesNac, int AñoNac,String FecIng,ArrayList<Embarcaciones> Embarcaciones,ArrayList<Puertos> Puertos){
    super(Nombre,Cedula,Direccion,Telefono,DiaNac,MesNac,AñoNac);
    this.FechaIngreso=FecIng;
    this.Embarcaciones=new ArrayList <>(Embarcaciones);
    this.Puertos=new ArrayList<>(Puertos);
    }
    //getter and setter

    public String getFechaIngreso() {
        return FechaIngreso;
    }

    public void setFechaIngreso(String FechaIngreso) {
        this.FechaIngreso = FechaIngreso;
    }

    public ArrayList<Embarcaciones> getEmbarcaciones() {
        return Embarcaciones;
    }

    public void setEmbarcaciones(ArrayList<Embarcaciones> Embarcaciones) {
        this.Embarcaciones = Embarcaciones;
    }

    public ArrayList<Puertos> getPuertos() {
        return Puertos;
    }

    public void setPuertos(ArrayList<Puertos> Puertos) {
        this.Puertos = Puertos;
    }
    
}
