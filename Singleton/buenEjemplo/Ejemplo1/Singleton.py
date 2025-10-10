from datetime import datetime, date

class Logger:
    __instance = None
    _logs: list[str] = []

    def __new__(cls):
        if not cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    
    def log(self, mensaje : str) -> None:
        self.logs.appemd(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensaje}")

        def show_logs(self) -> list[str]:
            return self.logs
        
class Usuario:
    def __init__(self, usuario_id: str, nombre: str) -> None:
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.pedidos = list["Pedido"] = []

    def registrar(self) -> None:
        logger = Logger()
        logger.log("El usuario {self.usuario_id} se registro")

    def agregarPedido(self, pedido: "Pedido") -> None:
        self.pedidos.append(pedido)
        logger = Logger()
        logger.log(f"El pedido {pedido.id} se agrego")

    def get_pedidos(self) -> list["Pedido"]:
        return self.pedidos

class Pedido:
    def __init__(self , pedido_id:int , fecha:date , precio:float) -> None:
        self.id = pedido_id
        self.fecha = fecha
        self.precio = precio
        self.estado = "Pendiente"
    
    def procesar(self) -> None:
        logger = Logger()
        logger.log(f"El pedido {self.id} se proceso")
        self.estado = "Procesado"

    def cancelar(self) -> None:
        logger = Logger()
        logger.log(f"El pedido {self.id} se cancela")
        self.estado = "Cancelado"
    
    def mostrarDetalles(self) -> str:
        return f"Pedido : {self.id} | fecha : {self.fecha} | precio : {self.precio} | estado : {self.estado}"
    
if __name__ == "__main__":
    Usuario = Usuario("1" , "Fernandito")
    Usuario.registrar()

    p1 = Pedido(1 , date(2022 , 1 , 1) , 100)

    Usuario.agregarPedido(p1)
    p1.procesar()

    p2 = Pedido(2 , date(2022 , 1 , 2) , 200)
    Usuario.agregarPedido(p2)
    p2.cancelar()

    print(f"Pedidos del usuario {Usuario.nombre}:")
    for pedido in Usuario.get_pedidos():
        print(pedido.mostrarDetalles())

    print("Registros del pedido 1:")
    for log in Logger.show_logs():
        print(log)

    print ("Registros del pedido 2:")
    for log in Logger.show_logs():
        print(log)
    
    print ("pedidos del usuario:")
    for pedido in Usuario.get_pedidos():
        print(pedido.mostrarDetalles())