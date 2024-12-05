/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package clase1septiembre;
import java.util.Scanner;
/**
 *
 * @author Estudiante
 */
public class CLASE1SEPTIEMBRE {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner objeto= new Scanner(System.in);
        System.out.println("Ingrese horas trabajadas");
        int horas = objeto.nextInt();
        System.out.println("Ingrese valor horas trabajadas");
        int valor = objeto.nextInt();
        int totalT=horas*valor;
        System.out.println("Total a pagar: "+totalT);
    }  
}
