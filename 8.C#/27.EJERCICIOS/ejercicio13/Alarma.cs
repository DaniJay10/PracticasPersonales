namespace coreObjectOrientedConcepts {
    internal class Alarma {
        public delegate void DelegadoAlarma();
        public event DelegadoAlarma OnAlarmaActivada ;

        public void VerificarAlarma(float temperatura){
            if(temperatura >= 4.75f){
                OnAlarmaActivada?.Invoke(); //llamamos al evento cuando se activa la alarma
            }
        }
    }
}