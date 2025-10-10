using System;

namespace conSLP
{
    public class SalarioFijo : iRemunerado
    {
        private readonly decimal _monto;

        public SalarioFijo(decimal monto)
        {
            _monto = monto;
        }

        public decimal CalcularSalario()
        {
            return _monto;
        }
    }
}