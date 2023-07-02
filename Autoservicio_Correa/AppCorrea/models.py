from django.db import models
from django.contrib.auth.models import User


# Pedidos
class MiPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre_apellido = models.CharField(max_length=100, null=True)
    fecha_pedido = models.DateField()
    horario_entrega = models.CharField(max_length=100)
    lugar_entrega = models.CharField(max_length=100)
    estado_pedido = models.CharField(max_length=50, default="Pendiente")
    detalle_pedido = models.TextField()

    class Meta:
        ordering = ['-fecha_pedido']


# Promociones
class Promocion(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    titulo_promo = models.CharField(max_length=100)
    descripcion_promo = models.TextField()
    precio_promo = models.DecimalField(max_digits=8, decimal_places=2)
    estado_promo = models.CharField(max_length=50)
    imagen_promo = models.ImageField(upload_to='imagenes_promo/', blank=True, null=True)

    def __str__(self):
        return f"Promo: {self.titulo_promo} \n - Fin: {self.fecha_fin} - Estado: {self.estado_promo} "
    
    def precio_promo_con_separador(self):
        return "{:,}".format(self.precio_promo)


# Comentarios
class Comentario(models.Model):
    comentario = models.ForeignKey(Promocion, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    mensaje = models.TextField(null=True, blank=True)
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha_comentario']

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Fecha: {self.fecha_comentario} - {self.comentario}  "




# Clases para evolutivos (NO es parte del Proyecto Final CODER)
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

class Pedido_basico(models.Model):
    cliente_pedido = models.CharField(max_length=100)
    fecha_pedido = models.DateField()
    horario_entrega = models.CharField(max_length=100)
    detalle_pedido = models.TextField()
    estado_pedido = models.CharField(max_length=50, default="Pendiente")

class Pedido(models.Model):
    cliente_pedido = models.CharField(max_length=100)
    fecha_pedido = models.DateField()
    horario_entrega = models.CharField(max_length=100)
    detalle_pedido = models.TextField()
    estado_pedido = models.CharField(max_length=50, default="Pendiente")