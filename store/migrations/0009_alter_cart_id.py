# Generated by Django 3.2.12 on 2022-04-03 03:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_review_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9ae37764-7a82-4940-94ee-4b3205fdf093'), primary_key=True, serialize=False),
        ),
    ]
