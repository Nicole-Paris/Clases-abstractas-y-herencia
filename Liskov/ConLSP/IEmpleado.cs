using System;

namespace conSLP;

public interface iEmpleado : iTrabajador
{
    string Nombre { get; set; }
    string Puesto { get; set; }


}