from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
   
    class Status(models.TextChoices):
        IMPORTED = 'imported', _('Imported')
        DRAFT = 'draft', _('Draft')
        
    code = models.CharField(verbose_name="Code", max_length=255, primary_key=True, db_index=True)
    barcode = models.CharField(verbose_name="Barcode", max_length=255, blank=True, null=True, db_index=True)
    status = models.CharField(verbose_name="Status", max_length=25, choices=Status.choices, default=Status.IMPORTED)
    imported_t = models.DateTimeField(verbose_name="Imported At", auto_now_add=True)
    url = models.URLField(verbose_name="Url", max_length=255)
    product_name = models.CharField(verbose_name="Name", max_length=255, db_index=True)
    quantity = models.CharField(verbose_name="Quantity", max_length=100, blank=True, null=True)
    categories = models.TextField(verbose_name="Categories", blank=True, null=True)
    packaging = models.CharField(verbose_name="Packaing", max_length=255, blank=True, null=True)
    brands = models.TextField(verbose_name="Brands", blank=True, null=True)
    image_url = models.URLField(verbose_name="Image Url", max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self) -> str:
        return self.product_name
