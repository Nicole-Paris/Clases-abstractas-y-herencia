using System;

namespace conSLP
{
    public class Program
    {
        public static void Main()
        {
            var sistema = new SistemaNominas();
            var empleado = new EmpleadoRegular
            {
                "Miguel",
                "Programador",
                new TrabajoTiempoCompleto(),
                new SalarioFijo(3000)
            };

            var pasante = new Pasante
            {
                "Ricardo",
                new TrabajoPasante()
            };

            console.WriteLine("Informacion de empleados");
            sistema.MostrarInfo(empleado);
            sistema.MostrarInfo(pasante);

            Console.WriteLine("\nTrabajo asignado");
            sistema.AsignarTrabajo(empleado);
            sistema.AsignarTrabajo(pasante);

            Console.WriteLine("\nSalario calculado");
            decimal salario = empleado.CalcularSalario();
            
         }
     }
 }
