/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package parcial2danieljay;

/**
 *
 * @author Estudiante
 */
public class MedioCampo extends Jugador {
    private int numAsistencias=0;
    //Constructor para asistencias predefinidas
    public MedioCampo(String Nom,int edad, String ciudad,boolean titular, int asistencias){
    super(Nom,edad,ciudad,titular);
    if(asistencias>0){
    this.numAsistencias=asistencias;
    }else{
    System.out.println("No se puede colocar asistencias negativas");
    }
    }
    //Constructor para asistencias no predefinidas
    public MedioCampo(String Nom,int edad, String ciudad,boolean titular){
    super(Nom,edad,ciudad,titular);
    }
     // metodo añadir assitencias
      public void adiccionarAsistencias(int asis) {
        if(asis>=0){
        System.out.println("Se adiccionaron "+asis+" asistencias a "+ getNombre());
        this.numAsistencias = this.numAsistencias+asis;
        }else{
        System.out.println("No se puede añadir asistencias negativas");
        }
    }

    public void verNumAsistencias() {
        System.out.println( "Total asistencias de "+getNombre()+" :" + numAsistencias );
    }
      
}
