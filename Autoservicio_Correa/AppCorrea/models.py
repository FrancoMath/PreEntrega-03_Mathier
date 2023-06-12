from django.db import models


# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    en_stock = models.CharField(max_length=5)
    en_promocion = models.CharField(max_length=5)

    def __str__(self):
        return f"Nombre: {self.nombre} \n - Precio: $ {self.precio}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField(max_length=40)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Direccion: {self.direccion}"


class Pedido_Basico(models.Model):
    cliente_pedido = models.CharField(max_length=100)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    horario_entrega = models.CharField(max_length=100)
    detalle_pedido = models.TextField()


# class Pedido(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     productos = models.ManyToManyField(Producto, through='DetallePedido')
#     fecha_pedido = models.DateTimeField(auto_now_add=True)
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Pedido: #{self.id} - Cliente: {self.cliente.nombre} - Fecha: {self.fecha_pedido}"

# class DetallePedido(models.Model):
#     pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
#     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
#     cantidad = models.PositiveIntegerField()
#     subtotal = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Detalle del Pedido #{self.pedido.id} - {self.producto.nombre}"

