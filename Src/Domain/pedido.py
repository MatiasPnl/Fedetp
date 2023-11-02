class Pedido:
    def __init__(self, nombre_cliente, detalles_pedido):
        self.nombre_cliente = nombre_cliente
        self.detalles_pedido = detalles_pedido

    def __str__(self):
        return f"Pedido de {self.nombre_cliente}: {', '.join(self.detalles_pedido)}"
