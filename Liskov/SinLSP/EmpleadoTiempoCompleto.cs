using System;

nameespace SinLSP;

public class EmpleadoTiempoCompleto : Empleado
{
    public override decimal CalcularSalario()
    {
        return 3000;
    }

    public override void Trabajar()
    {
        Console.WriteLine("Trabajando 8 horas diarias");
    }

    

}