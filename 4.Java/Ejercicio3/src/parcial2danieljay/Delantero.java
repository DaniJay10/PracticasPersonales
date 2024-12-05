/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package parcial2danieljay;

/**
 *
 * @author Estudiante
 */
public class Delantero extends Jugador {
    private int golesAnotados=0;
    //constructor goles predefinidos
    public Delantero(String Nom,int edad, String ciudad,boolean titular,int goles){
    super(Nom,edad,ciudad,titular);
    if(goles>0){
    this.golesAnotados=goles;
    }else{
    System.out.println("No se puede colocar goles negativos");
    }
    }
    //constructor goles sin predefinir
     public Delantero(String Nom,int edad, String ciudad,boolean titular){
    super(Nom,edad,ciudad,titular);
    }
     
     //metodo
    public void adiccionarGoles(int goles) {
        if(goles>=0){
        System.out.println("Se adiccionaron "+goles+" goles a "+ getNombre());
        this.golesAnotados = this.golesAnotados+goles;
        }else{
        System.out.println("No se puede añadir goles negativos");
        }
    }
    
     public void verGoles() {
        System.out.println( "Total goles de "+getNombre()+" :" + golesAnotados );
    }
}
