# Generated by Django 4.2.1 on 2023-05-14 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=100)),
                ("user_phone_number", models.CharField(max_length=20)),
                ("pickup_point_address", models.CharField(max_length=200)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("In Progress", "In Progress"),
                            ("Ready for Pickup", "Ready for Pickup"),
                            ("Picked Up", "Picked Up"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductTag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("slug", models.CharField(max_length=100, unique=True)),
                ("address", models.CharField(max_length=200)),
                ("phone_number", models.CharField(max_length=20)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="stores/%Y/%m/%d"
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("Grocery", "Grocery"),
                            ("Pharmacy", "Pharmacy"),
                            ("Clothing", "Clothing"),
                            ("Electronics", "Electronics"),
                            ("Furniture", "Furniture"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="products/%Y/%m/%d"
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="stores.store",
                    ),
                ),
                ("tags", models.ManyToManyField(to="stores.producttag")),
            ],
        ),
        migrations.CreateModel(
            name="OrderProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.IntegerField(default=1)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stores.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="stores.product"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                through="stores.OrderProduct", to="stores.product"
            ),
        ),
    ]
