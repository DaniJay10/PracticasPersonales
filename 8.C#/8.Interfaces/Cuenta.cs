namespace coreObjectOrientedConcepts {
public class Cuenta : BankAccount {
  
  public double saldo;

  public Cuenta(){
    saldo = 100;
  }
  public void depositar(){
    Console.WriteLine("Ingrese la cantidad a depositar:");
    double deposito = double.Parse(Console.ReadLine());
    saldo += deposito;
    Console.WriteLine($"Saldo después del deposito: {saldo}");
  }

  public void retirar(){
    Console.WriteLine("Ingrese la cantidad a retirar:");
    double retiro = double.Parse(Console.ReadLine());
    if(retiro <= saldo){
      saldo -= retiro;
      Console.WriteLine($"Saldo después del retiro: {saldo}");
    }else{
      Console.WriteLine("Saldo insuficiente");
    }
  }

  public void balance(){
    Console.WriteLine($"Saldo actual: {saldo}");
  }

}
}