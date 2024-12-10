using coreObjectOrientedConcepts;

Indexer peliculas = new Indexer();
peliculas[0] = "Harry popoter";
peliculas[1] = "matrix";
peliculas[2] = "vengadores";
peliculas[3] = "Sonic";

for(int i=0; i<peliculas.Length; i++){
    Console.WriteLine(peliculas[i]);
}