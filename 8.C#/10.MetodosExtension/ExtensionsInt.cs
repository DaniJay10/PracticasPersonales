namespace coreObjectOrientedConcepts
{
    static class ExtensionsInt{

    
     public static int Duplicar(this int numero)
    {
        return numero * 2;
    }

    public static bool IsGreaterThan(this int numero, int value){
        return numero > value;
    }
}
}