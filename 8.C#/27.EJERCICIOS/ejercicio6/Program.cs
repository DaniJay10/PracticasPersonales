using System.Text;
/*Crea un programa que genere e imprima una matriz identidad de tamaño 3x3. 
Temas: Matrices, Bucles.*/



//Matriz 3x3
int[,] matriz = new int[3,3] {{1,2,3}, {4,5,6} ,{7,8,9}};
for(int i = 0; i <= 2; i++){
   for(int j = 0; j <= 2; j++){
    Console.Write(matriz[i, j] + "\t");
   }
   Console.WriteLine();
}

//Matriz 2x2 llenada por el usuario
int[,] matriz2 = new int[2,2];
for(int i = 0; i <= 1; i++){
    for (int j = 0; j <= 1; j++){
        Console.WriteLine($"Ingrese numero posicion: {i}{j}");
        matriz2[i, j] = int.Parse(Console.ReadLine());
    }
}

for(int i=0; i <= 1; i++){
    for(int j=0; j <= 1; j++){
        Console.Write(matriz2[i, j] + "\t");
    }
    Console.WriteLine();
}