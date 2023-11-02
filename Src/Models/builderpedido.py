from pedido import Pedido

class BuilderPedido:
    def crear_pedido(self, nombre_cliente, detalles_pedido):
        if self._verificar_detalles(detalles_pedido):
            return Pedido(nombre_cliente, detalles_pedido)
        return None

    def _verificar_detalles(self, detalles_pedido):
        return len(detalles_pedido) > 0
