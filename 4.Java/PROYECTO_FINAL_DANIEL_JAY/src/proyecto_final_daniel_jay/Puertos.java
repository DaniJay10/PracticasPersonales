/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto_final_daniel_jay;

/**
 *
 * @author Estudiante
 */
public class Puertos {
    private int NumPuerto;
    private double Ancho;
    private boolean ServiciosContratados;
    private Socio Socio;
    private Embarcaciones Embarcacion;
    private String fechaCompraPuerto;
    //Contructor para puerto sin dueño
    public Puertos(int Numero, double Ancho, boolean Mantenimiento){
    this.NumPuerto=Numero;
    this.Ancho=Ancho;
    this.ServiciosContratados=Mantenimiento;
    }
    //Contructor para puerto con dueño pero sin embarcacion
    public Puertos(int Numero, double Ancho, boolean Mantenimiento,Socio Socio,String fechaCompra){
    this.NumPuerto=Numero;
    this.Ancho=Ancho;
    this.ServiciosContratados=Mantenimiento;
    this.Socio=Socio;
    this.fechaCompraPuerto=fechaCompra;
    }
    //Constructor para puerto con Embarcacion
    public Puertos(int Numero, double Ancho, boolean Mantenimiento,Socio Socio,String fechaCompra, Embarcaciones Embarcacion){
    this.NumPuerto=Numero;
    this.Ancho=Ancho;
    this.ServiciosContratados=Mantenimiento;
    this.Socio=Socio;
    this.fechaCompraPuerto=fechaCompra;
    this.Embarcacion=Embarcacion;
    }
    
    //getter and setter

    public int getNumPuerto() {
        return NumPuerto;
    }

    public void setNumPuerto(int NumPuerto) {
        this.NumPuerto = NumPuerto;
    }

    public double getAncho() {
        return Ancho;
    }

    public void setAncho(double Ancho) {
        this.Ancho = Ancho;
    }

    public boolean isServiciosContratados() {
        return ServiciosContratados;
    }

    public void setServiciosContratados(boolean ServiciosContratados) {
        this.ServiciosContratados = ServiciosContratados;
    }

    public Socio getSocio() {
        return Socio;
    }

    public void setSocio(Socio Socio) {
        this.Socio = Socio;
    }

    public Embarcaciones getEmbarcacion() {
        return Embarcacion;
    }

    public void setEmbarcacion(Embarcaciones Embarcacion) {
        this.Embarcacion = Embarcacion;
    }

    public String getFechaCompraPuerto() {
        return fechaCompraPuerto;
    }

    public void setFechaCompraPuerto(String fechaCompraPuerto) {
        this.fechaCompraPuerto = fechaCompraPuerto;
    }
    
    
}
