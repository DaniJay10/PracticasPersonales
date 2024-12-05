/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package CentroSalud;

/**
 *
 * @author Estudiante
 */
public class Persona {
    private int nif;
    private String nombre;
    private int annio;
    private int mes;
    private int dia;
    
    public Persona (int nif, String nombre, int año, int month, int day){
    this.nif=nif;
    this.nombre=nombre;
    this.annio=año;
    this.mes=month;
    this.dia=day;
    }
    
    public Persona (int nif, String nombre){
    this.nif=nif;
    this.nombre=nombre;
    }
    //metodos
    
    public int calcularEdad(){
    int edad=0;
    edad=2023-this.annio;
    if(this.mes<10 && this.dia<4){
    edad=edad-1;
    }
    return edad;
    }
    
    public boolean EsMayor(){
    if(this.calcularEdad()>=18){
    return true;
    }else{
     return false;
    }
    }
    
}
