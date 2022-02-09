# Generated by Django 3.2.10 on 2022-01-26 06:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('name', models.CharField(max_length=100, verbose_name='商品名')),
                ('price', models.PositiveIntegerField(verbose_name='価格')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('name', models.CharField(max_length=20, verbose_name='カテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='登録日時')),
                ('image', models.ImageField(upload_to='shop/product_image/image/', verbose_name='商品画像')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.product', verbose_name='対象商品')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.productcategory', verbose_name='カテゴリ'),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('category', 'name')},
        ),
    ]
