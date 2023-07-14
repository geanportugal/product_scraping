# Generated by Django 4.1.10 on 2023-07-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False, verbose_name='Code')),
                ('barcode', models.CharField(blank=True, db_index=True, max_length=255, null=True, verbose_name='Barcode')),
                ('status', models.CharField(choices=[('imported', 'Imported'), ('draft', 'Draft')], default='imported', max_length=25, verbose_name='Status')),
                ('imported_t', models.DateTimeField(auto_now_add=True, verbose_name='Imported At')),
                ('url', models.URLField(max_length=255, verbose_name='Url')),
                ('product_name', models.CharField(db_index=True, max_length=255, verbose_name='Name')),
                ('quantity', models.CharField(blank=True, max_length=100, null=True, verbose_name='Quantity')),
                ('categories', models.TextField(blank=True, null=True, verbose_name='Categories')),
                ('packaging', models.CharField(blank=True, max_length=255, null=True, verbose_name='Packaing')),
                ('brands', models.TextField(blank=True, null=True, verbose_name='Brands')),
                ('image_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='Image Url')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]