/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package parcial2danieljay;

import java.util.ArrayList;

/**
 *
 * @author Estudiante
 */
public class Equipo {
    private String Nombre;
    private double numJuegos;
    private double numGanados;
    private double numPerdidos;
    private DirectorTecnico Tecnico;
    private ArrayList<Jugador> Jugadores = new ArrayList<Jugador>();
    
    public Equipo(String Nom, double Juegos, double Jganados, double Jperdidos, DirectorTecnico Tecnico, ArrayList<Jugador> jugadores){
    if(jugadores.size()<11){
    System.out.println("ERROR el equipo no cuenta con 11 jugadores");
    System.out.println("Numero de jugadores: "+jugadores.size());
    }else{
    this.Nombre=Nom;
    this.numJuegos=Juegos;
    this.numGanados=Jganados;
    this.numPerdidos=Jperdidos;
    this.Tecnico=Tecnico;
    for(int i=0;i<jugadores.size();i++){
    Jugadores.add(jugadores.get(i));
    }
    }}
    
    
    //Añadir Jugadores
    public void añadirJugador(Jugador J){
    Jugadores.add(J);
    }
    //metodos
    public void aumentarNumGanados(double numGanados) {
     if(Jugadores.size()<11){
    System.out.println("Errorrrr el equipo no puede jugar hasta tener minimo 11 jugadores, favor agregar con metodo añadirJugador");
    }else{
    if(numGanados>=0){
    System.out.println("Partidos jugados y partidos ganados: "+this.numJuegos + " y "+this.numGanados + " Respectivamente");
    this.numGanados = this.numGanados+numGanados;
    this.numJuegos = this.numJuegos+numGanados;
    System.out.println("Partidos jugados y partidos ganados: "+this.numJuegos + " y "+this.numGanados + " Respectivamente");
    }else{
    System.out.println("ERROR, no se puede añadir partidos ganados negativos");
    }}}

    public void aumentarNumPerdidos(double numPerdidos) {
     if(Jugadores.size()<11){
    System.out.println("Errorrrr el equipo no puede jugar hasta tener minimo 11 jugadores, favor agregar con metodo añadirJugador");
    }else{
     if(numPerdidos >=0){
      System.out.println("Partidos jugados y partidos perdidos: "+this.numJuegos + " y "+this.numPerdidos + " Respectivamente");
    this.numPerdidos = this.numPerdidos + numPerdidos;
    this.numJuegos = this.numJuegos+numPerdidos;
      System.out.println("Partidos jugados y partidos perdidos: "+this.numJuegos + " y "+this.numPerdidos + " Respectivamente");
    }else{
     System.out.println("ERROR, no se puede añadir partidos perdidos negativos");
     }}}
    
    public void Efectividad(){
    if(Jugadores.size()<11){
    System.out.println("Errorrrr el equipo no puede jugar hasta tener minimo 11 jugadores, favor agregar con metodo añadirJugador");
    }else{
    double e = 100*(this.numGanados/this.numJuegos);
    System.out.println("La efectividad de "+this.Nombre+" es: "+e+"%");
    }}
    
    //setters

    public void setNombre(String Nombre) {
        this.Nombre = Nombre;
    }

    //getters

    public String getNombre() {
        return Nombre;
    }

    public double getNumJuegos() {
       return numJuegos;
    }

    public double getNumGanados() {
        return numGanados;
    }

    public double getNumPerdidos() {
        return numPerdidos;
    }
    
}
