from datetime import datetime, date

class Logger:
    def __init__(self):
        self.logs = []

    def log(self , message: str) -> None:
        self.logs.append(f "[{datetime.strftime(datetime.now(), '%H:%M:%S')}] {message}") # type: ignore

    def show_logs(self) -> list[str]:
        return self.logs
    

class Usuario:
    def __init__(self, usuario_id: str, nombre: str) -> None:
        self.usuario_id = usuario_id
        self.nombre = nombre
        self.pedidos = list["Pedido"] = []
        self.logger = Logger()

    def registrar(self) -> None:
        self.logger.log(f"Usuario {self.usuario_id} registrado")

    def agergarPedido(self, pedido: "Pedido") -> None:
        self.pedidos.append(pedido)
        self.logger.log(f"Pedido {pedido.id} agregado")

    def get_pedidos(self) -> list["Pedido"]:
        return self.pedidos


class Pedido:
    def __init__(self , pedido_id:int , fecha:date , precio:float) -> None:
        self.id = pedido_id
        self.fecha = fecha
        self.precio = precio
        self.estado = "Pendiente"
        self.logger = Logger()

    def procesar(self) -> None:
        self.estado = "Procesado"
        self.logger.log(f"Pedido {self.id} procesado")
    
    def cancelar(self) -> None:
        self.estado = "Cancelado"
        self.logger.log(f"Pedido {self.id} cancelado")
    
    def mostrarDetalles(self) -> str:
        return f"Pedido : {self.id} | fecha : {self.fecha} | precio : {self.precio} | estado : {self.estado}"
    
if __name__ == "__main__":
    Usuario = Usuario("1" , "Fernandito")
    Usuario.registrar()

    p1 = Pedido(1 , date(2022 , 1 , 1) , 100)

    Usuario.agergarPedido(p1)
    p1.procesar()

    p2 = Pedido(2 , date(2022 , 1 , 2) , 200)
    Usuario.agergarPedido(p2)
    p2.cancelar()

    print(f"Pedidos del usuario {Usuario.nombre}:")
    for pedido in Usuario.get_pedidos():
        print(pedido.mostrarDetalles())

    print("Registros del pedido 1:")
    for log in p1.logger.show_logs():
        print(log)

    print ("Registros del pedido 2:")
    for log in p2.logger.show_logs():
        print(log)


    