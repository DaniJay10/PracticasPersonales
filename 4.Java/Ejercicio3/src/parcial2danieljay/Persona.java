/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package parcial2danieljay;

/**
 *
 * @author Estudiante
 */
public abstract  class Persona {
    private String Nombre;
    private int Edad;
    private String Ciudad;
    public Persona(String Nom,int edad, String ciudad){
    this.Nombre=Nom;
    //VALIDADOR EDAD
    if(edad>=18 && edad<=40){
    this.Edad=edad;
    }else{
    System.out.println("ERRORRR!!! la edad debe ser entre 18 y 40 años");
    }
    this.Ciudad=ciudad;
    }
    
    
     public Persona(String Nom, String ciudad){
    }
    
    
    //getters

    public String getNombre() {
        return Nombre;
    }

    public int getEdad() {
        return Edad;
    }

    public String getCiudad() {
        return Ciudad;
    }
    //setters

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public void setEdad(int Edad) {
        this.Edad = Edad;
    }

    public void setCiudad(String Ciudad) {
        this.Ciudad = Ciudad;
    }
    
}
