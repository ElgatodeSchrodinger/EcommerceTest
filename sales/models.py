from django.db import models


class Customer(models.Model):
    """Customer Model."""

    id = models.AutoField(primary_key=True)

    name = models.CharField(verbose_name="Nombres", max_length=150)

    lastname = models.CharField(verbose_name="Apellidos", max_length=150)

    identification_number = models.CharField(verbose_name="DNI", max_length=20)

    email = models.EmailField(verbose_name="Email", max_length=200)

    def __str__(self):
        return self.name + ' ' + self.lastname

    class Meta:

        verbose_name = "Cliente"

        verbose_name_plural = "Clientes"


class Category(models.Model):
    """Category Model."""

    id = models.AutoField(primary_key=True)

    name = models.CharField(verbose_name="Nombre de la categoría", max_length=100)

    parent_categ_id = models.ForeignKey('self', verbose_name="Categoría Padre", on_delete=models.CASCADE,
                                        blank=True, null=True)

    icon = models.ImageField(upload_to="sales/categories", blank=True)

    def __str__(self):
        return "[" + self.parent_categ_id.name + "]" + self.name if self.parent_categ_id else self.name

    class Meta:

        verbose_name = "Categoría"

        verbose_name_plural = "Categorías"


class Product(models.Model):
    """Product Model."""

    id = models.AutoField(primary_key=True)

    categ_id = models.ForeignKey(Category, verbose_name="Categoría", on_delete=models.CASCADE)

    name = models.CharField(verbose_name="Nombre del Producto", max_length=200)

    image = models.ImageField(upload_to="sales/products", blank=True)

    price = models.FloatField(verbose_name="Precio del Producto")

    stock = models.IntegerField(verbose_name="Stock")

    def __str__(self):
        return self.name

    @property
    def quantitysold(self):
        order_lines = SaleOrderLine.objects.filter(product_id=self.id, order_id__state__contains='process')
        if order_lines:
            return sum([orderline.quantity for orderline in order_lines])
        else:
            return 0

    class Meta:

        verbose_name = "Producto"

        verbose_name_plural = "Productos"


class SaleOrder(models.Model):
    """Sale Order Model."""

    STATES = [
        ('cart', 'En Carrito'),
        ('process', 'Procesado'),
        ('cancel', 'Cancelado')
    ]

    id = models.AutoField(primary_key=True)

    created_date = models.DateField(verbose_name="Fecha de creación", auto_now_add=True)

    state = models.CharField(verbose_name="Estado", choices=STATES, max_length=10, default='cart')

    customer = models.ForeignKey(Customer, verbose_name="Cliente", on_delete=models.CASCADE, null=True, blank=True)

    total_amount = models.FloatField(verbose_name="Precio Total")

    @property
    def total_amount(self):
        order_lines = SaleOrderLine.objects.filter(order_id=self.id)
        if order_lines:
            return sum([order_line.product.price * order_line.quantity for order_line in order_lines])
        else:
            return 0

    class Meta:

        verbose_name = "Orden de Venta"

        verbose_name_plural = "Ordenes de Venta"


class SaleOrderLine(models.Model):
    """Sale Order Line Model."""

    id = models.AutoField(primary_key=True)

    order_id = models.ForeignKey(SaleOrder, verbose_name="Orden de Venta", on_delete=models.CASCADE)

    product_id = models.ForeignKey(Product, verbose_name="Producto", on_delete=models.CASCADE)

    quantity = models.IntegerField(verbose_name="Cantidad")

    class Meta:

        verbose_name = "Linea de Orden de Venta"

        verbose_name_plural = "Lineas de Ordenes de Venta"
