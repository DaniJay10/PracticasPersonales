/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package parcial2danieljay;

/**
 *
 * @author Estudiante
 */
public abstract class Jugador extends Persona{
    private boolean EsTitular;
    private Equipo equipo;
    //constructor para jugador sin equipo
    public Jugador(String Nom,int edad, String ciudad,boolean titular){
    super(Nom,edad,ciudad);
    this.EsTitular=titular;
    }
     //constructor para jugador que le queremos agregar un equipo
    public Jugador(String Nom,int edad, String ciudad,boolean titular, Equipo equipo){
    super(Nom,edad,ciudad);
    this.EsTitular=titular;
    this.equipo=equipo;
    }
}
