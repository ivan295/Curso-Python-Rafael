class Productos:

    def __init__(self, id, nombre, grupo, subgrupo):
        self.id = id
        self.nombre = nombre
        self.grupo = grupo
        self.subgrupo = subgrupo

    def __str__(self):
        return 'Producto :{} {} {} {}'.format(self.id, self.nombre, self.grupo, self.subgrupo)


class Admin(Productos):
    productos = []

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return 'admin {} {}'.format(self.id, self.nombre)

    def verProductos(self):
        for showp in self.productos:
            print(f"productos : {showp}")

    def agregarProductos(self, producto):
        self.productos.append(producto)

    def eliminarProducto(self, product):
        try:
            self.productos.remove(product)
        except ValueError as error:
            print("tipo de error : ", error.__class__)
            print("el elemento que desea eliminar no existe")
        else:
            print("el dato se elmino exitosamente")

    def modificarProducto(self, producto_search, producto_update):
        for ind, dato in enumerate(self.productos):
            if dato == producto_search:
                self.productos[ind] = producto_update

    def realizar_envio(self):
        return 'se esta realizando el envio de tipo {}'.format(type(self))

    def confirmar_entrega(self):
        return 'entrega confirmada'


class Cliente(Productos):
    carrito = []

    def __init__(self, id, nombre, direccion, phno):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.phno = phno

    def __str__(self):
        return '{} {} {} {}'.format(self.id, self.nombre, self.direccion, self.phno)

    def comprar_productos(self, productocarrito):
        self.carrito.append(productocarrito)

    def ver_productos(self):
        for showc in self.carrito:
            print(f"productos en el carrito : {showc}")

    def realizar_pago(self):
        return 'pago realizado con exito'

    def agregar_cesta(self):
        return 'producto añadido a la cesta'

    def eliminar_cesta(self):
        return 'producto eliminado con exito'


class Invitado(Productos):
    def ver_productos(self):
        return 'lista de productos'

    def registro(self):
        return 'seccion de registro'


class Pago(Cliente):
    def __init__(self, idcliente, nombre, tipo_tarjeta, no_tarjeta):
        self.idcliente = idcliente
        self.nombre = nombre
        self.tipo_tarjeta = tipo_tarjeta
        self.no_tarjeta = no_tarjeta

    def __str__(self):
        return '{} {} {} {}'.format(self.idcliente, self.nombre, self.tipo_tarjeta, self.no_tarjeta)


class Carro(Cliente):
    def __init__(self, id, num_productos, producto1, producto2, producton, precio, total):
        self.id = id
        self.num_productos = num_productos
        self.producto1 = producto1
        self.producto2 = producto2
        self.producton = producton
        self.precio = precio
        self.total = total

    def __str__(self):
        return '{} {} {} {} {} {} {}'.format(self.id, self.num_productos, self.producto1, self.producto2, self.producton, self.precio, self.total)


if __name__ == "__main__":
    # por falta de tiempo tengo que hacerlo lo mas sencillo
    # se presentaron inconvenientes en el transcurso de la semana y tuve que hacerlo lo mas
    # rapido posible, gracias de antemano y mil disculpas
    ad = Admin(1, 'ivan')
    ad.agregarProductos('computadora')  # agregando producto
    # ingresar el nombre del producto que desea eliminar
    ad.eliminarProducto('computador')
    ad.verProductos()
    # primer argumento es el dato a modificar y el segundo es el nuevo dato
    ad.modificarProducto('computadora', 'mouse')
    ad.verProductos()
    ad.realizar_envio()
    ad.confirmar_entrega()
