namespace ConceptosBasicos
{
    internal class Codigo
    {
        public delegate void DelegadoMensaje();

        public void EjecutarMetodo(DelegadoMensaje metodo) //aqui le estamos diciendo que para ejecutar el metodo
        {                                                  //debemos pasarle un delegado como parametro. En este caso
            metodo();                                      // con el nombre metodo
        }
    }
}
