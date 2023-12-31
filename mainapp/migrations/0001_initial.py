# Generated by Django 4.2.6 on 2023-10-09 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('images', models.ImageField(null=True, upload_to='user/profile_pic')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChapaTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('amount', models.FloatField()),
                ('currency', models.CharField(default='ETB', max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('payment_title', models.CharField(default='Payment', max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('created', 'CREATED'), ('pending', 'PENDING'), ('success', 'SUCCESS'), ('failed', 'FAILED')], default='created', max_length=50)),
                ('response_dump', models.JSONField(blank=True, default=dict)),
                ('checkout_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Chapa Transaction',
                'verbose_name_plural': 'Chapa Transactions',
            },
        ),
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone_no', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Headline', models.CharField(max_length=1000)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCatagory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('images', models.ImageField(null=True, upload_to='user/profile_pic')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.catagory')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('images', models.ImageField(null=True, upload_to='user/profile_pic')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.IntegerField()),
                ('cattagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.catagory')),
                ('subcatagory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.subcatagory')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderuniqueId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('aproved', 'aproved'), ('pending', 'pending'), ('declined', 'declined')], default='pending', max_length=10)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.customerprofile')),
                ('order_items', models.ManyToManyField(blank=True, related_name='order_items', to='mainapp.orderitems')),
            ],
        ),
        migrations.AddField(
            model_name='orderitems',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product'),
        ),
    ]
