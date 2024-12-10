using coreAdvancedConcepts;

CalculateDelegate c1 = new CalculateDelegate(DelegateExample.addition);

CalculateDelegate c2 = new CalculateDelegate(DelegateExample.subtraction);


CalculateDelegate c3 = new CalculateDelegate(DelegateExample.multiplication);

c1(100);
Console.WriteLine(DelegateExample.getNumber());
c2(77);
Console.WriteLine(DelegateExample.getNumber());
c3(2);
Console.WriteLine(DelegateExample.getNumber());


//Delegate multicast : Cada delegate puede apuntar a mas de 1 metodo.
c1 += new CalculateDelegate(DelegateExample.multiplication);
c1(9);
Console.WriteLine(DelegateExample.getNumber());