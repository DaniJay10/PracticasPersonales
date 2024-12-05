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
public class Zona {
    private char NombreZona;
    private String TipoBarcos;
    private double Profundidad;
    private ArrayList<Puertos> Puertos = new ArrayList<Puertos>();
    private ArrayList<Empleado> Empleados = new ArrayList<Empleado>();
    //Zona sin empleados
    public Zona (char Nombre, String TipoBarcos, double Profundidad,ArrayList<Puertos> Puertos){
    this.NombreZona=Nombre;
    this.TipoBarcos=TipoBarcos;
    this.Puertos=new ArrayList<>(Puertos);
    }
    //Zona con empleados
        public Zona (char Nombre, String TipoBarcos, double Profundidad,ArrayList<Puertos> Puertos,ArrayList<Empleado> Empleados){
    this.NombreZona=Nombre;
    this.TipoBarcos=TipoBarcos;
    this.Puertos=new ArrayList<>(Puertos);
    this.Empleados=new ArrayList <>(Empleados);
    }
    //Metodo calcular embarcaciones de la zona
    public String barcosZona(){
    int numBarcos =0;
    for(int j=0;j<this.Puertos.size();j++){
    if(this.Puertos.get(j).getEmbarcacion() != null){
    numBarcos +=1;
    }
    }
    return "La zona "+ this.NombreZona + " tiene "+ numBarcos +" Barcos";
    }
    //metodo para calcular ancho promedio
    public String anchoPromedio(){
    double sumaAn =0;
    for(int j=0;j<this.Puertos.size();j++){
    sumaAn = sumaAn  + this.Puertos.get(j).getAncho();
    }
    double Promedio = sumaAn/this.Puertos.size();
    return "La zona "+ this.NombreZona + " tiene un promedio de ancho correspondiente a: "+ Promedio;
    }

    public char getNombreZona() {
        return NombreZona;
    }

    public void setNombreZona(char NombreZona) {
        this.NombreZona = NombreZona;
    }

    public String getTipoBarcos() {
        return TipoBarcos;
    }

    public void setTipoBarcos(String TipoBarcos) {
        this.TipoBarcos = TipoBarcos;
    }

    public double getProfundidad() {
        return Profundidad;
    }

    public void setProfundidad(double Profundidad) {
        this.Profundidad = Profundidad;
    }

    public ArrayList<Puertos> getPuertos() {
        return Puertos;
    }

    public void setPuertos(ArrayList<Puertos> Puertos) {
        this.Puertos = Puertos;
    }

    public ArrayList<Empleado> getEmpleados() {
        return Empleados;
    }

    public void setEmpleados(ArrayList<Empleado> Empleados) {
        this.Empleados = Empleados;
    }
    
}