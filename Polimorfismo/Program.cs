using System;
using TiposdePolimorfismo.Figuras;
using TiposdePolimorfismo.Unidades;
using TiposdePolimorfismo.Utilidades
using TiposdePolimorfismo.Genericos;

class Program
{
    public static void Main(String[] args)
    {
        List<Figura> figuras = new List<Figura>()
        {
            new Circulo(1),
            new Rectangulo(1, 2)
        };

        foreach (Figura f in figuras)
        {
            f.Dibujar();
            Console.WriteLine($"Área: {f.Area()}");

        }

        Caja<int> caja1 = new Caja<int>();
        caja1.Agregar(1);
        caja1.Agregar(2);
        Console.WriteLine($"Contenido de la caja: {string.Join(", ", caja1.ObtenerContenido())}");

        Calculadora calc = new Calculadora();
        Console.WriteLine($"Suma: {calc.Sumar(1, 2)}");
        Console.WriteLine($"Resta: {calc.Restar(5, 3)}");
        
    }
}