using System;

namespace SinLSP;

public class Pasante : Empleado
{
    public override decimal CalcularSalario()
    {
        throw new NotImplementedException("Los pasantes no reciben salario");
    }

    public override void Trabajar()
    {
        console.WriteLine("Aprendiendo y trabajando");
    }
    
}