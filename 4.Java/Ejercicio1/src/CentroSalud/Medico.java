/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package CentroSalud;

/**
 *
 * @author Estudiante
 */
public class Medico extends Persona{
    private String titulo;
    private String TipoMedico;
    private String provincia;
    private String horario;
    
    public Medico(int nif, String nombre, String direccion, int telefono, char sexo,
            String titulo, String TipoMedico, String provincia, String horario,int año, int mes, int dia){
    super(nif,nombre, direccion, telefono, sexo,año,mes,dia);
    this.titulo=titulo;
    this.TipoMedico=TipoMedico;
    this.provincia=provincia;
    this.horario=horario;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getTipoMedico() {
        return TipoMedico;
    }

    public void setTipoMedico(String TipoMedico) {
        this.TipoMedico = TipoMedico;
    }

    public String getProvincia() {
        return provincia;
    }

    public void setProvincia(String provincia) {
        this.provincia = provincia;
    }

    public String getHorario() {
        return horario;
    }

    public void setHorario(String horario) {
        this.horario = horario;
    }
    
}
