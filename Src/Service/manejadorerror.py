class ManejadorError:
    def __init__(self):
        self.siguiente = None

    def manejar_error(self):
        if self.siguiente:
            self.siguiente.manejar_error()

class ManejadorErrorBuilder(ManejadorError):
    def manejar_error(self):
        print("Error en la construcción del pedido")
        super().manejar_error()

class ManejadorErrorBaseDeDatos(ManejadorError):
    def manejar_error(self):
        print("Error en la base de datos de pedidos")
        super().manejar_error()