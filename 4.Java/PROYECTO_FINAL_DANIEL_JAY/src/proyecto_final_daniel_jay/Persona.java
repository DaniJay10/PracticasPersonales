/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto_final_daniel_jay;

/**
 *
 * @author Estudiante
 */
public abstract class Persona {
    private String Nombre;
    private int Cedula;
    private String Direccion;
    private int telefono;
    private int DiaNacimiento;
    private int MesNacimiento;
    private int AñoNacimiento;
    //Contructor
    public Persona(String Nombre, int Cedula, String Direccion,int Telefono, int DiaNac, int MesNac, int AñoNac){
    this.Nombre=Nombre;
    this.Cedula=Cedula;
    this.Direccion=Direccion;
    this.telefono=Telefono;
    this.DiaNacimiento=DiaNac;
    this.MesNacimiento=MesNac;
    this.AñoNacimiento=AñoNac;
    }
    //Metodo Calcular edad
    public String CalularEdad(){
    //La fecha esta calculada tomando como referencia el 10 de noviembre del 2023
    int edad = 2023-this.AñoNacimiento;
    if(this.MesNacimiento>10){
    if(this.DiaNacimiento>10){
    edad = edad-1;
    }
    }
    return "La edad de "+this.Nombre+" es: "+edad;
    }
    
    //Getter and Setter

    public String getNombre() {
        return Nombre;
    }

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    public int getCedula() {
        return Cedula;
    }

    public void setCedula(int Cedula) {
        this.Cedula = Cedula;
    }

    public String getDireccion() {
        return Direccion;
    }

    public void setDireccion(String Direccion) {
        this.Direccion = Direccion;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono) {
        this.telefono = telefono;
    }

    public int getDiaNacimiento() {
        return DiaNacimiento;
    }

    public void setDiaNacimiento(int DiaNacimiento) {
        this.DiaNacimiento = DiaNacimiento;
    }

    public int getMesNacimiento() {
        return MesNacimiento;
    }

    public void setMesNacimiento(int MesNacimiento) {
        this.MesNacimiento = MesNacimiento;
    }

    public int getAñoNacimiento() {
        return AñoNacimiento;
    }

    public void setAñoNacimiento(int AñoNacimiento) {
        this.AñoNacimiento = AñoNacimiento;
    }
    
    }
