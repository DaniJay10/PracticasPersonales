#include <stdio.h>
int main(){
    float altura, peso;
    printf("Ingrese la altura: ");
    scanf("%f", &altura);
    printf("Ingrese su peso: ");
    scanf("%f", &peso);
    float masaCorporal;
    masaCorporal = peso / (altura * altura);
    if (masaCorporal < 18.5){
        printf("Peso por debajo de lo normal");
    } else if(masaCorporal >= 18.5 && masaCorporal <= 25){
        printf("Peso normal");
    }else if(masaCorporal > 25 && masaCorporal <= 30){
        printf("Tiene sobrepeso");
    }
    else if(masaCorporal > 30){
        printf("Obesidad");
    }
    return 0;
}