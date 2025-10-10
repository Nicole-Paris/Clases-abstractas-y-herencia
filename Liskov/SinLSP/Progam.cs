using System;

namespace SinLSP;

public class Program
{
    public static void Main()
    {
        Empleado e1 = new EmpleadoTiempoCompleto();
        Empleado e2 = new Pasante();

        Console.WriteLine("Empleado a tiempo completo: ");
        Console.WriteLine($"Salario : {e1.CalcularSalario()}");
        e1.Trabajar();

        Console.WriteLine("Empleado pasante: ");
        try
        {
            Console.WriteLine($"Salario : {e2.CalcularSalario()}");
        }
        catch (InvalidOperationException e)
        {
            Console.WriteLine($"Error : {e.Message}");
        }
        e2.Trabajar();

    }
}