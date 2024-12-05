/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package CentroSalud;

/**
 *
 * @author Jay
 */
public class Cita {
    public Medico medico;
    public Paciente paciente;
    private String fecha;
    private String hora;
    private String tipo;
    private int numConsultorio;
    
    public Cita(Medico med, Paciente pac,String fecha, String hora, String tipo, int NumCon){
    this.medico = med;
    this.paciente = pac;
    this.fecha = fecha;
    this.hora = hora;
    this.tipo = tipo;
    this.numConsultorio=NumCon;
    }

    public Medico getMedico() {
        return medico;
    }

    public void setMedico(Medico medico) {
        this.medico = medico;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

    public String getFecha() {
        return fecha;
    }

    public void setFecha(String fecha) {
        this.fecha = fecha;
    }

    public String getHora() {
        return hora;
    }

    public void setHora(String hora) {
        this.hora = hora;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getNumConsultorio() {
        return numConsultorio;
    }

    public void setNumConsultorio(int numConsultorio) {
        this.numConsultorio = numConsultorio;
    }
    
}
