#include <stdio.h>
int main (){
   float Nota1, Nota2;
   printf("Ingrese nota del primer examen: ");
   scanf("%f",&Nota1);
   printf("Ingrese nota del Segundo examen: ");
   scanf("%f",&Nota2);
   float NotaFinal;
   NotaFinal = (Nota1+Nota2)/2;
   printf("La nota final es: %.2f",NotaFinal);//el punto 2 es para indicar el numero de decimales que queremos ver
   return 0;
}
