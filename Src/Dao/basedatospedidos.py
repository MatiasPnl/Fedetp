class BaseDeDatosPedidos:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(BaseDeDatosPedidos, cls).__new__(cls)
            cls._instance.pedidos = []
        return cls._instance

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def mostrar_pedidos(self):
        for pedido in self.pedidos:
            print(pedido)
