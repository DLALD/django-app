from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class DateTimeModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Client(DateTimeModel):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    celular = models.CharField(max_length=15)
    password = models.CharField(max_length=128)  # Almacenar contraseña encriptada

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)  # Encriptar la contraseña antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Product(DateTimeModel):
    nombre_producto = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_producto

class ClientProduct(DateTimeModel):
    id_cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    numero_cuenta = models.CharField(max_length=50)

class TransactionType(DateTimeModel):
    nombre = models.CharField(max_length=100)
    abreviatura = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Transaction(DateTimeModel):
    id_cliente_producto = models.ForeignKey(ClientProduct, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_transaccion = models.ForeignKey(TransactionType, on_delete=models.CASCADE)

    def __str__(self):
        monto_formateado = "${:,.2f}".format(self.monto)
        return f"Transacción {self.id} - Monto: {monto_formateado}"
