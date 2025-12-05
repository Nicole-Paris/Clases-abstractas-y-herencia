using System;

public class Reproductor
{
    public void encender()
    {
        Console.WriteLine("Reproductor encendido.");
    }

    public void apagar()
    {
        Console.WriteLine("Reproductor apagado.");
    }

    public void reproducir(string pelicula)
    {
        Console.WriteLine($"Reproduciendo {pelicula}.");
    }

    public void pausar()
    {
        Console.WriteLine("Reproductor pausado.");
    }
}