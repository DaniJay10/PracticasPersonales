/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package coche;

/**
 *
 * @author Estudiante
 */
public class Coche {
    private String color;
    private float velocidad;
    private float tamaño;
    
    public Coche (String color, float velocidad, float tamaño){
    this.color = color;
    this.velocidad = velocidad;
    this.tamaño = tamaño;
    }
    public void avanzar(float vel , float dist){
    System.out.println("El coche avanza con velocidad igual a: "+vel+" Y distancia igual a: "+dist);
    }
    public void parar(int tiempo){}
    public void girarIzquierda(float angulo){}
    public void girarDerecha(float angulo){}

    public static void main(String[] args) {
        Coche miCoche = new Coche ("verde",80,3.2f);
        Coche tuCoche = new Coche ("azul",90,3.1f);
        Coche suCoche = new Coche ("rojo",75,3f);
    }
    
}
