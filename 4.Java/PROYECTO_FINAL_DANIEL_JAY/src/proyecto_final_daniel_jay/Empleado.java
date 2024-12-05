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
public class Empleado extends Persona{
   private int Codigo;
   private String Especialidad;
   private ArrayList<Zona> Zonas = new ArrayList<Zona>();
   private ArrayList<Embarcaciones> Embarcaciones = new ArrayList<Embarcaciones>();
   //Constructor Empleado zon zonas
    public Empleado(String Nombre, int Cedula, String Direccion,int Telefono, int DiaNac, 
    int MesNac, int AñoNac, int Cod, String Esp, ArrayList<Zona> Zonas){
    super(Nombre,Cedula,Direccion,Telefono,DiaNac,MesNac,AñoNac);
    this.Codigo=Cod;
    this.Especialidad=Esp;
    this.Zonas=new ArrayList<>(Zonas);
    }
    //Constructor empleado con embarcaciones por aparte de las zonas
    public Empleado(String Nombre, int Cedula, String Direccion,int Telefono, int DiaNac, 
    int MesNac, int AñoNac, int Cod, String Esp, ArrayList<Zona> Zonas,ArrayList<Embarcaciones> Embarcaciones){
    super(Nombre,Cedula,Direccion,Telefono,DiaNac,MesNac,AñoNac);
    this.Codigo=Cod;
    this.Especialidad=Esp;
    this.Zonas=new ArrayList<>(Zonas);
    this.Embarcaciones=new ArrayList<>(Embarcaciones);
    }
    
    //Metodo calcular tiempo de trabajo 
    public String CalcularTiempoTrabajo(int AñoIngreso, int MesIngreso, int DiaIngreso){
    //(En dias) (En base a la fecha 10/11/2023)
    //Calcular dias de años que trabajo
    int diasPreliminares= 365*(2023-AñoIngreso-1);
    //Calcular dias que trabajo el primer año
    int diasPrimerAño=365-((MesIngreso-1)*30+DiaIngreso);
    //Calcular dias que ha trabajado en el 2023
    int diasAñoActual=(11-1)*30+10;
    //Calcular dias extras (Años bisciestos)
    int diasExtras=0;
    int Años=0;
    for(int i=AñoIngreso;i<2023;i++){
    Años +=1;
    if(i%4==0){
    diasExtras += 1;
    }
    }
    int dias=diasPreliminares + diasAñoActual + diasPrimerAño + diasExtras;
    // Calcular dias habiles (de lunes a sabado) y festivos
    //calcular dias festivos que tuvo el primer año
    //festivos si entro a trabajar en enero
    int festivosPrimerAño=0;
    if(MesIngreso==1){
    if(DiaIngreso>1){
    festivosPrimerAño=17;
    }else{
    festivosPrimerAño=18;
    }if(DiaIngreso>1){
    festivosPrimerAño=16;
    }else{
    festivosPrimerAño=17;
    }
    }
    //Marzo suponiendo que el festivo es el 20 de marzo
    if(MesIngreso==3){
    if(DiaIngreso>20){
    festivosPrimerAño=15;
    }else{
    festivosPrimerAño=16;
    }
    }
    //Abril suponiendo que los festivos son 2-6
    if(MesIngreso==4){
    if(DiaIngreso>2){
    festivosPrimerAño=14;
    }else{
    festivosPrimerAño=15;
    }if(DiaIngreso>6){
    festivosPrimerAño=13;
    }else{
    festivosPrimerAño=14;
    }
    }
    //Mayo suponiendo que los festivos son el 1 y el 22
    if(MesIngreso==5){
    if(DiaIngreso>1){
    festivosPrimerAño=12;
    }else{
    festivosPrimerAño=13;
    }if(DiaIngreso>22){
    festivosPrimerAño=11;    
    }else{
    festivosPrimerAño=12;
    }
    }
    //Junio suponiendo los festivos son el 12 y el 19
    if(MesIngreso==6){
    if(DiaIngreso>12){
    festivosPrimerAño=10;
    }else{
    festivosPrimerAño=11;
    }if(DiaIngreso>19){
    festivosPrimerAño=9;
    }else{
    festivosPrimerAño=10;
    }
    }
    //Julio suponinedo que los festivos son el 3 y el 20
    if(MesIngreso==7){
    if(DiaIngreso>3){
    festivosPrimerAño=8;
    }else{
    festivosPrimerAño=9;
    }if(DiaIngreso>20){
    festivosPrimerAño=7;
    }else{
    festivosPrimerAño=8;
    }
    }
    //Agosto suponiendo que los festivos son 7 y 21
    if(MesIngreso==8){
    if(DiaIngreso>7){
    festivosPrimerAño=6;
    }else{
    festivosPrimerAño=7;
    }if(DiaIngreso>21){
    festivosPrimerAño=5;
    }else{
    festivosPrimerAño=6;
    }
    }
   //Octubre suponiendo que los festivos son el 16
    if(MesIngreso==10){
    if(DiaIngreso>16){
    festivosPrimerAño=4;
    }else{
    festivosPrimerAño=5;
    }
    }
   //Noviembre suponiendo que los festivos son 6 y 13
    if(MesIngreso==11){
    if(DiaIngreso>6){
    festivosPrimerAño=3;
    }else{
    festivosPrimerAño=4;
    }if(DiaIngreso>13){
    festivosPrimerAño=2;
    }else{
    festivosPrimerAño=3;
    }
    }
    //Diciembre suponiendo que los festivos son 8 y 25
    if(MesIngreso==12){
    if(DiaIngreso>8){
    festivosPrimerAño=1;
    }if(DiaIngreso>25){
    festivosPrimerAño=0;
    }
    }
    
    
    int diasHabiles = dias-(dias/7)-18*(Años-1)-15-festivosPrimerAño;
    return "Han pasado "+dias+" dias desde que "+this.getNombre()+" entro a trabajar. De los cuales "+diasHabiles+" fueron dias que trabajo";
    
    }
    //getter and setter

    public int getCodigo() {
        return Codigo;
    }

    public void setCodigo(int Codigo) {
        this.Codigo = Codigo;
    }

    public String getEspecialidad() {
        return Especialidad;
    }

    public void setEspecialidad(String Especialidad) {
        this.Especialidad = Especialidad;
    }

    public ArrayList<Zona> getZonas() {
        return Zonas;
    }

    public void setZonas(ArrayList<Zona> Zonas) {
        this.Zonas = Zonas;
    }

    public ArrayList<Embarcaciones> getEmbarcaciones() {
        return Embarcaciones;
    }

    public void setEmbarcaciones(ArrayList<Embarcaciones> Embarcaciones) {
        this.Embarcaciones = Embarcaciones;
    }
    
    
    }
