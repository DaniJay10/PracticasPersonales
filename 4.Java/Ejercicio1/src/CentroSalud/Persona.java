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
    private String direccion;
    private int telefono;
    private char sexo;
    private int annio;
    private int mes;
    private int dia;
    
    public Persona (int nif, String nombre, String direccion, int telefono, char sexo, int año, int mes, int dia){
    this.nif=nif;
    this.nombre=nombre;
    this.direccion=direccion;
    this.telefono=telefono;
    this.sexo=sexo;
    this.annio=año;
    }

    public int getNif() {
        return nif;
    }

    public void setNif(int nif) {
        this.nif = nif;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getDireccion() {
        return direccion;
    }

    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public char getSexo() {
        return sexo;
    }

    public void setSexo(char sexo) {
        this.sexo = sexo;
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
    
}
