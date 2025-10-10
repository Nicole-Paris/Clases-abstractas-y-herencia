package BadExample;
public class App {
    public static void main(String[] args) throws Exception {
        Caricatura Homero = new Caricatura("Homero");
        Caricatura Bart = new Caricatura("Bart");
        
        Simpson.hablar(Homero);
        Simpson.hablar(Bart);
    }
}
