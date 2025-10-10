using System;

namespace conSLSP
{
    public class Pasantes : iEmpleado
    {
        public string Nombre { get; }
        public string Puesto { get; }

        private readonly iTrabajador _trabajador;

        public Pasantes(string nombre, string puesto, iTrabajador trabajador)
        {
            Nombre = nombre;
            Puesto = puesto;
            _trabajador = trabajador;
        }

        public void Trabajar()
        {
            _trabajador.Trabajar();
        }
    }
}