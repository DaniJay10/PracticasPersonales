namespace coreObjectOrientedConcepts
{
    static class String{

    
     public static int ContadorPlabras(this string cadena)
    {
        int contador = 0;

        string [] partesOracion = cadena.Split(' ');
        foreach ( string parte in partesOracion){
            contador += 1;  
        }

        return contador;
    }


}
}