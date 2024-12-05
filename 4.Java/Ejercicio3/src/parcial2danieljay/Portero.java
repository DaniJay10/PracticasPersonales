/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package parcial2danieljay;

/**
 *
 * @author Estudiante
 */
public class Portero extends Jugador{
    private int golesTapados=0;
    //Constructor en caso de que se desee predefinir las atajadas
    public Portero(String Nom,int edad, String ciudad,boolean titular,int atajadas){
    super(Nom,edad,ciudad,titular);
    if(atajadas>0){
    this.golesTapados=atajadas;
    }else{
    System.out.println("No se puede colocar atajadas negativas");
    }
    }
    //Constructor en caso se desee inicializar las atajadas en 0
    public Portero(String Nom,int edad, String ciudad,boolean titular){
    super(Nom,edad,ciudad,titular);
    }
    //metodo agregar atajadas 

    public void adiccionarGolesTapados(int atajadas) {
        if(atajadas>=0){
        System.out.println("Se adiccionaron "+atajadas+" atajadas a "+ getNombre());
        this.golesTapados = this.golesTapados+atajadas;
        }else{
        System.out.println("No se puede añadir atajas negativas");
        }
    }

    public void verGolesTapados() {
        System.out.println( "Total atajadas de "+getNombre()+" :" +golesTapados);
    }
    
    
    
}
