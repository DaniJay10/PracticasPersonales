// array
using System.Text;

int[] barca = new int[3] {1,2,3};
foreach(int i in barca){
    Console.WriteLine(i);
}

//Matriz
int[,] matriz = new int[3,3] {{1,2,3}, {4,5,6} ,{7,8,9}};
for(int i = 0; i <= 2; i++){
   for(int j = 0; j <= 2; j++){
    Console.Write(matriz[i, j] + "\t");
   }
   Console.WriteLine();
}

//jagged array
int[][]jaggedArray = new int [2][];
jaggedArray[0]= new int[2]{1,2};
jaggedArray[1]= new int[3]{3,4,5};
for (int i = 0; i < jaggedArray.Length; i++) 
{
  for (int j = 0; j < jaggedArray[i].Length; j++)
    {
    Console.Write(jaggedArray[i][j] + "\t");
    }
    Console.WriteLine(); 
}

//strings
Console.WriteLine();
string str1 = "hello world";
string str2 = "C# programming";
Console.WriteLine(str1);
Console.WriteLine(str1.Length);
string str3 = string.Concat(str1, str2);
Console.WriteLine(str3);
Console.WriteLine(str1.Equals(str2));
Console.WriteLine(str1.ToLower());
Console.WriteLine(str1.ToUpper());
Console.WriteLine(str1.EndsWith("w"));
Console.WriteLine(str1.IndexOf("o"));
Console.WriteLine(str1.Contains("w"));
Console.WriteLine(str1.Insert(2, "insercion"));
Console.WriteLine(str1.CompareTo(str2));
Console.WriteLine(str1.Clone());

//cadena inmutable
string str5 = "Messi";
//cadena mutable: la cadena mutable puedo agregar todo el contenido que quiera sin necesidad de concatenar dos cadenas.
StringBuilder stringBuilder = null;
stringBuilder.Append("Messi");
stringBuilder.Append("Iniesta");