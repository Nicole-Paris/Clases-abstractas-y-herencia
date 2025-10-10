public class App {
    public static void main(String[] args) throws Exception {
        SistemaPedidos pedidos = new SistemaPedidos("Elias", "Americano");
        MaquinaCafe cafe = new MaquinaCafe("Americano");
        Factura factur = new Factura("Elias", 82.50);
        Notificacion notifi = new Notificacion("Elias", "Tu pedido está listo");


        pedidos.tomarPedido();
        cafe.prepararCafe();
        factur.generarFactura();
        notifi.enviarMensaje();
    }
}
