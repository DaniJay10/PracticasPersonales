#include <stdio.h>
int main (){
    int edad;
    printf("Ingrese su edad: ");
    scanf("%d",&edad);
    if(edad >= 18){
        printf("Es mayor de edad");
    }else{
        printf("Es menor de edad");
    }
     return 0;
}