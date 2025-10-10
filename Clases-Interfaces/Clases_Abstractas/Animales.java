package ClasesInterfaces.Clases_Abstractas;

public abstract class Animales {
    protected String name;

    public Animales(String name) {
        this.name = name;
    }

    public abstract void hacerRuido();

    public void dormir(){
        System.out.println(this.name + " está dormido ");
    }

    public String getName() {
        return name;
    }
}
