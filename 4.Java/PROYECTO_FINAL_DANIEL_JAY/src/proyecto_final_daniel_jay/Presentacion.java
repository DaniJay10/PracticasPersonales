/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package proyecto_final_daniel_jay;

import java.util.ArrayList;

/**
 *
 * @author Estudiante
 */
public class Presentacion {
    public static void main(String[] args) {
    //toda esta presentacion estara mas explicada en el video
    //PRUEBA BARCO
    System.out.println("Prueba EMBARCACIONES");
    Embarcaciones Barco1 = new Embarcaciones("Titan",12,"Turistico",23.6,56);
    //imprimir un atributo
    System.out.println(Barco1.getDimension());
    Embarcaciones Barco2 = new Embarcaciones("Destructor",12,"Turistico",23,56);
    //crear lista de embarcaciones para crear un socio
    ArrayList<Embarcaciones> EmbarcacionesP = new ArrayList<Embarcaciones>(); 
    EmbarcacionesP.add(Barco1);
    EmbarcacionesP.add(Barco2);
    
    
    
    
    //PRUEBA SOCIOS 
     System.out.println("Prueba SOCIO");
    Socio Pablo = new Socio("Pablo",1,"calle 23",234432,11,11,2003,"14/08/2023",EmbarcacionesP);
    //imprimir un atributo
    System.out.println(Pablo.getCedula());
    //probar metodo calcular edad
    System.out.println(Pablo.CalularEdad());
    
    
    
    
    
    //PRUEBA PUERTOS
    System.out.println("Prueba PUERTOS");
    Puertos Puerto1 = new Puertos(23,123.4,false,Pablo,"12/04/2023",Barco1);
    //imrpimir un atributo
     System.out.println(Puerto1.getAncho());
    Puertos Puerto2 = new Puertos(23,56.4,false,Pablo,"12/04/2023");
    Puertos Puerto3 = new Puertos(23,99.3,false,Pablo,"12/04/2023",Barco2);
    //DATO: Hemos creado 3 puertos, pero dos de ellos poseen un barco asignado, ahora lo agregaremos a un arraylist
    ArrayList<Puertos> PuertosPrueba = new ArrayList<Puertos>(); 
    PuertosPrueba.add(Puerto1);
    PuertosPrueba.add(Puerto2);
    PuertosPrueba.add(Puerto3);
    
    
    
    
    
    //PRUEBA ZONA
    System.out.println("Prueba ZONAS");
    Zona Zona1 =new Zona('V',"Turisticos",324.3,PuertosPrueba);
    //imprimimos un atributo
    System.out.println(Zona1.getTipoBarcos());
    //prueba de los dos metodos de zona
    System.out.println(Zona1.barcosZona());
    System.out.println(Zona1.anchoPromedio());
    //agregaremos la zona agregada a un arraylist para poder crear la clase empleado
    ArrayList<Zona> ZonasTrabajo = new ArrayList<Zona>(); 
    ZonasTrabajo.add(Zona1);
     
    
    //PRUEBA EMPLEADOS
     System.out.println("Prueba EMPLEADOS");
    Empleado Pedro = new Empleado("Pedro",2,"calle 15",34543,15,2,2000,12,"Cuidador",ZonasTrabajo);
    //imprimimos un atributo
    System.out.println(Pedro.getCodigo());
    //prueba metodo tiempo de trabajo
    System.out.println(Pedro.CalcularTiempoTrabajo(2018,10,11));
    
    
    
    //pruebas extras de polimorfismo (explicada a mas detalle en el video)
      //polimorfismo puertos
    Puertos Puerto4 = new Puertos(23,123.4,false,Pablo,"17/08/2023"); 
    //polimorfismo zona
    ArrayList<Empleado> Empleado = new ArrayList<Empleado>(); 
    Empleado.add(Pedro);
    Zona Zona2 =new Zona('V',"Turisticos",324.3,PuertosPrueba,Empleado);
    ArrayList<Embarcaciones> EmbarcacionesP2 = new ArrayList<Embarcaciones>(); 
    //polimorfismo embarcaciones
     Embarcaciones Barco3 = new Embarcaciones("Omega",12,"Turistico",23,56);
    EmbarcacionesP2.add(Barco3);
    //polimorfismo empleados
    Empleado Paco = new Empleado("Paco",2,"calle 15",34543,15,2,2000,12,"Cuidador",ZonasTrabajo,EmbarcacionesP2);
    //Polimorfismo socios
     Socio Yeimy = new Socio("Yeimy",1,"calle 23",234432,11,11,2003,"14/08/2023",EmbarcacionesP2,PuertosPrueba);
}
}
