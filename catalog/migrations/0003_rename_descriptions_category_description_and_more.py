# Generated by Django 5.0.7 on 2024-08-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descriptions',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
