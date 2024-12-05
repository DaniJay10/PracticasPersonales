/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package CentroSalud;
/**
 *
 * @author Estudiante
 */
public class Paciente extends Persona{
    private int estrato;
    private String MedicoAsignado;
    
    public Paciente(int nif, String nombre, String direccion, int telefono, char sexo, int estrato, String MedicoAsignado,int año, int mes, int dia){
       super(nif,nombre, direccion, telefono, sexo,año,mes,dia);
       this.estrato=estrato;
       this.MedicoAsignado=MedicoAsignado;
    }

    public int getEstrato() {
        return estrato;
    }

    public void setEstrato(int estrato) {
        this.estrato = estrato;
    }

    public String getMedicoAsignado() {
        return MedicoAsignado;
    }

    public void setMedicoAsignado(String MedicoAsignado) {
        this.MedicoAsignado = MedicoAsignado;
    }
    
}
