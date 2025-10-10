package ClasesInterfaces.Clases;

public class Perro {
    private int edad;
    private String nombre;

    public Perro(int edad, String nombre) {
        this.edad = edad;
        this.nombre = nombre;
    }

    public void ladrar(){
        System.out.println("Wow wow");
    }

    public void comer(){
        System.out.println(this.nombre + " esta comiendo");
    }

    public void dormir(){
        System.out.println(this.nombre + "esta dormido");
    }

    
}
