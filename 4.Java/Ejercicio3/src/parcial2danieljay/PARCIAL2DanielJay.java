/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package parcial2danieljay;

import java.util.ArrayList;

/**
 *
 * @author Estudiante
 */
public class PARCIAL2DanielJay {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        //Tecnico
        DirectorTecnico PepGuardiola = new DirectorTecnico("Pep",40,"B",15);
        
        //Portero
        //System.out.println("PRUEBA PORTERO");
        Portero Valdes = new Portero("Valdes",34,"A",true);
        //Valdes.verGolesTapados();
       // Valdes.adiccionarGolesTapados(24);
       // Valdes.verGolesTapados();
        //MedioCampista
        //System.out.println("PRUEBA MEDIOCAMPISTA");
        MedioCampo Iniesta = new MedioCampo("Iniesta",20,"v",true);
        //Iniesta.verNumAsistencias();
        //Iniesta.adiccionarAsistencias(12);
        //Iniesta.verNumAsistencias();
        //Iniesta.adiccionarAsistencias(8);
        //Iniesta.verNumAsistencias();
        
        //Delantero
        //System.out.println("PRUEBA DELANTERO");
        Delantero Messi = new Delantero("Messi",23,"R",true,23);
        //Messi.verGoles();
        //Messi.adiccionarGoles(-1);
        //Messi.verGoles();
        
        ArrayList<Jugador> jugadores = new ArrayList<Jugador>(); 
        jugadores.add(Valdes);
        jugadores.add(Iniesta);
        jugadores.add(Messi);
        MedioCampo Xavi = new MedioCampo("Xavi",20,"v",true);
        jugadores.add(Xavi);
        MedioCampo Busi = new MedioCampo("Busi",20,"v",true);
         jugadores.add(Busi);
        MedioCampo Pique = new MedioCampo("Pique",20,"v",true);
         jugadores.add(Pique);
        MedioCampo Puyol = new MedioCampo("Puyol",20,"v",true);
        jugadores.add(Puyol);
        MedioCampo Alves = new MedioCampo("Alves",20,"v",true);
         jugadores.add(Alves);
        MedioCampo Abidal = new MedioCampo("Abidal",20,"v",true);
         jugadores.add(Abidal);
        Delantero Villa = new Delantero("Villa",23,"R",true); 
         jugadores.add(Villa);
        Delantero Pedro = new Delantero("Pedro",23,"R",true);
         jugadores.add(Pedro);
        
        
        //Equipo
        Equipo Bucaros = new Equipo("Bucaros",24,12,12,PepGuardiola,jugadores);
        Bucaros.Efectividad();
        Bucaros.aumentarNumGanados(7);
        Bucaros.Efectividad();
        Bucaros.aumentarNumPerdidos(-5);
        Bucaros.Efectividad();
       


}   
}
