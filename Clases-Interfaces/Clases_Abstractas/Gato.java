package ClasesInterfaces.Clases_Abstractas;

public class Gato extends Animales{
    
    public Gato(String name){
        super(name);
    }

    @Override
    public void hacerRuido() {
        System.out.println("Meow");
        
    }

    


}
