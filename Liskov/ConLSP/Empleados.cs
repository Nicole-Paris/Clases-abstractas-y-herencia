using System;

namespace conSLSP
{
    public class EmppleadoRegular : iEmpleado, Iremunerado
    {
        public string Nombre { get; }
        public string Puesto { get; }

        private readonly iTrabajador _trabajador;
        private readonly iRemunerado _remunerado;

        public EmppleadoRegular(string nombre, string puesto, iTrabajador trabajador, iRemunerado remunerado)
        {
            Nombre = nombre;
            Puesto = puesto;
            _trabajador = trabajador;
            _remunerado = remunerado;
        }

        public void Trabajar()
        {
            _trabajador.Trabajar();
        }

        public decimal CalcularSalario()
        {
            return _remunerado.CalcularSalario();
        }
    }
}