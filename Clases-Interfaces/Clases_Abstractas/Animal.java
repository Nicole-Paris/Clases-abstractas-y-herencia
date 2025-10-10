package ClasesInterfaces.Clases_Abstractas;

public abstract class Animal {
    protected boolean isAlive = true;
    protected int age;
    public Animal(int age) {
        this.age = age;
        this.isAlive = true;
    }

    public abstract void hacerRuido();
    
    
}
