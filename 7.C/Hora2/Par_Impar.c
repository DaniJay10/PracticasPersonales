#include <stdio.h>
int main(){
    int numeros;
    printf("Ingrese un numero");
    scanf("%d", &numeros);
    if((numeros % 2) == 0){
        printf("El numero es par");
    }else{
        printf("El numero es impar");
    }
    return 0;
}