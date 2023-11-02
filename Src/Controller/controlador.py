from pedido import Pedido
from basedatospedidos import BaseDeDatosPedidos
from vista import Vista

class Controlador:
    def __init__(self):
        self.builder_pedido = BuilderPedido()
        self.base_de_datos_pedidos = BaseDeDatosPedidos()
        self.vista = Vista()

    def realizar_pedido(self, nombre_cliente, detalles_pedido):
        pedido = self.builder_pedido.crear_pedido(nombre_cliente, detalles_pedido)
        if pedido:
            self.base_de_datos_pedidos.agregar_pedido(pedido)
            self.vista.mostrar_pedido_realizado(pedido)
        else:
            self.vista.mostrar_error()