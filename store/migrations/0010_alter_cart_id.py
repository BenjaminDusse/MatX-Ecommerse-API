# Generated by Django 3.2.12 on 2022-04-03 03:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('29fef370-fbec-44ce-9e55-dfc7e91bcb0a'), primary_key=True, serialize=False),
        ),
    ]