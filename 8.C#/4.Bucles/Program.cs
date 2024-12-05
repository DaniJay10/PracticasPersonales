string[] names = new string [] {"Daniel Jay", "Yuliana Gonzalez", "Yeimy Corzo", "Sirly Esteban", "Mariana Peña"};
//FOR
Console.WriteLine("-------------------------------------------------------------");
for(int i=0; i<names.Length; i++){
    Console.WriteLine(names[i]);
} 

//FOREACH
Console.WriteLine("-------------------------------------------------------------");
foreach(string name in names){
    Console.WriteLine(name);
}
//WHILE
Console.WriteLine("-------------------------------------------------------------");
int contador = 0;
while(contador < names.Length) {
    Console.WriteLine(names[contador]);
    contador++;
}
//DO WHILE
Console.WriteLine("-------------------------------------------------------------");
int contador2 = 0;
do {
    Console.WriteLine(names[contador2]);
    contador2++;
}while(contador2 < names.Length);