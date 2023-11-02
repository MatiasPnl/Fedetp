from pedido_dao import PedidoDAO

class ServicioPedido:
    def __init__(self, pedido_dao: PedidoDAO):
        self.pedido_dao = pedido_dao

    def procesar_pedido(self, pedido_id):
        pedido = self.pedido_dao.obtener_pedido_por_id(pedido_id)
        costo_total = self.calcular_costo_total(pedido)
        pedido.costo_total = costo_total


        self.pedido_dao.guardar_pedido(pedido)

    def calcular_costo_total(self, pedido):
        costo_total = 0
        for item in pedido.items:
            costo_total += item.precio * item.cantidad

        return costo_total
