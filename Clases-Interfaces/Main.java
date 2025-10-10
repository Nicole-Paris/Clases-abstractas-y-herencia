package ClasesInterfaces;
import ClasesInterfaces.Clases_Abstractas.Camion;
import ClasesInterfaces.Clases.Perro;
import ClasesInterfaces.Clases_Abstractas.Pato;

public class Main {

    public static void main(String[] args) {

        Camion miCamion = new Camion("Nissan", 4, "Blanco", 4);
        miCamion.acelerar();
        miCamion.encender();

        System.out.println(" - - - - - - - --  -- ");

        Perro miPerrito = new Perro(5, "Rocky");
        miPerrito.comer();
        miPerrito.dormir();
        miPerrito.ladrar();

        System.out.println( "- - - -- - - - -- - - - -" );

        Pato miPatito = new Pato(2, "Blanco");
        miPatito.hacerRuido();
        miPatito.volar();

        

    }
}

