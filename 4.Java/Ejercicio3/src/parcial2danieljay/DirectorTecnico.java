/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package parcial2danieljay;

/**
 *
 * @author Estudiante
 */
public class DirectorTecnico extends Persona {
    private int annioExperiencia;
    private  Equipo equipo;
    //constructor para tecnico sin equipo
    public DirectorTecnico(String Nom,int edad, String ciudad, int experiencia){
    super(Nom,edad,ciudad);
    //VALIDADOR EXPERIENCIA
    if(experiencia<getEdad()){
    this.annioExperiencia=experiencia;
    }else{
    System.out.println("ERRORR !!! La experiencia es superior a la edad");
    }
    }
    //constructor para tecnico agregandole un equipo
    public DirectorTecnico(String Nom,int edad, String ciudad, int experiencia,Equipo equipo){
    super(Nom,edad,ciudad);
    //VALIDADOR EXPERIENCIA
    if(experiencia<this.getEdad()){
    this.annioExperiencia=experiencia;
    }else{
    System.out.println("ERRORR !!! La experiencia es superior a la edad");
    }
    this.equipo=equipo;
    }

    public int getAnnioExperiencia() {
        return annioExperiencia;
    }

    public void setAnnioExperiencia(int annioExperiencia) {
        this.annioExperiencia = annioExperiencia;
    }
    
    
}
