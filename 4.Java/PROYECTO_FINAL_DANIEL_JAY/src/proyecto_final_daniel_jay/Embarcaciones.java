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
public class Embarcaciones {
    private String Nombre;
    private int Matricula;
    private String Tipo;
    private double Dimension;
    private double Volumen;
    private Socio Socio;
    private Puertos Puerto;
    private String fechaAsignacion;
    private ArrayList<Empleado> Empleados = new ArrayList<Empleado>();
    
    //Constructor para embarcacion sin dueño, sin puerto, sin empleados
   public Embarcaciones(String Nombre, int Matricula, String Tipo, double Dimension, double V3){
    this.Nombre=Nombre;
    this.Matricula=Matricula;
    this.Tipo=Tipo;
    this.Dimension=Dimension;
    this.Volumen=V3;
    }
    //constructor para embarcacion con puerto pero sin dueño (socio)
    public Embarcaciones(String Nombre, int Matricula, String Tipo, double Dimension, double V3,Puertos Puerto,String FechaAsigPuerto){
    this.Nombre=Nombre;
    this.Matricula=Matricula;
    this.Tipo=Tipo;
    this.Dimension=Dimension;
    this.Volumen=V3;
    this.Puerto=Puerto;
    this.fechaAsignacion=FechaAsigPuerto;
    }
    //constructor para embarcaciones con puerto y con dueño (socio)
     public Embarcaciones(String Nombre, int Matricula, String Tipo, double Dimension, double V3,Puertos Puerto,String FechaAsigPuerto, Socio Socio){
    this.Nombre=Nombre;
    this.Matricula=Matricula;
    this.Tipo=Tipo;
    this.Dimension=Dimension;
    this.Volumen=V3;
    this.Puerto=Puerto;
    this.fechaAsignacion=FechaAsigPuerto;
    this.Socio=Socio;
    }
   //constructor para embarcacion sin dueño pero con puerto y empleados asignados
    public Embarcaciones(String Nombre, int Matricula, String Tipo, double Dimension, double V3,Puertos Puerto,String FechaAsigPuerto,ArrayList<Empleado> Empleados){
    this.Nombre=Nombre;
    this.Matricula=Matricula;
    this.Tipo=Tipo;
    this.Dimension=Dimension;
    this.Volumen=V3;
    this.Puerto=Puerto;
    this.fechaAsignacion=FechaAsigPuerto;
    this.Empleados=new ArrayList <>(Empleados);
    }
   //constructor para embarcaciones con puerto,dueño y empleados asignados
    public Embarcaciones(String Nombre, int Matricula, String Tipo, double Dimension, double V3,Puertos Puerto,String FechaAsigPuerto, Socio Socio,ArrayList<Empleado> Empleados){
    this.Nombre=Nombre;
    this.Matricula=Matricula;
    this.Tipo=Tipo;
    this.Dimension=Dimension;
    this.Volumen=V3;
    this.Puerto=Puerto;
    this.fechaAsignacion=FechaAsigPuerto;
    this.Socio=Socio;
    this.Empleados=new ArrayList <>(Empleados);
    } 
     
    //getter and setter

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public int getMatricula() {
        return Matricula;
    }

    public void setMatricula(int Matricula) {
        this.Matricula = Matricula;
    }

    public String getTipo() {
        return Tipo;
    }

    public void setTipo(String Tipo) {
        this.Tipo = Tipo;
    }

    public double getDimension() {
        return Dimension;
    }

    public void setDimension(double Dimension) {
        this.Dimension = Dimension;
    }

    public double getVolumen() {
        return Volumen;
    }

    public void setVolumen(double Volumen) {
        this.Volumen = Volumen;
    }

    public Socio getSocio() {
        return Socio;
    }

    public void setSocio(Socio Socio) {
        this.Socio = Socio;
    }

    public String getFechaAsignacion() {
        return fechaAsignacion;
    }

    public void setFechaAsignacion(String fechaAsignacion) {
        this.fechaAsignacion = fechaAsignacion;
    }

    public Puertos getPuerto() {
        return Puerto;
    }

    public void setPuerto(Puertos Puerto) {
        this.Puerto = Puerto;
    }

    public ArrayList<Empleado> getEmpleados() {
        return Empleados;
    }

    public void setEmpleados(ArrayList<Empleado> Empleados) {
        this.Empleados = Empleados;
    }
    
    }
