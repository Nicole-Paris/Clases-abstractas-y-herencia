


class manejadorDatos:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializacndo
        return cls._instancia
    
    def cargar(self) -> dict: 
        with open(self.archivo , "r") as f:
            lector = csv.reader(f)
        return (fila [1] for fila in lector)