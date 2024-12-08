namespace coreObjectOrientedConcepts {
internal interface BankAccount {


   void depositar();
   void retirar();
   void balance(); //Al ser una interfaz todas las clases son publicas y abstractas por defecto.
}
}