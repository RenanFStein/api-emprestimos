# Generated by Django 4.0.6 on 2022-08-09 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agrofacil', '0017_remove_vendas_produto_remove_vendas_quantidade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='estoque',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agrofacil.estoque', verbose_name='Estoque'),
            preserve_default=False,
        ),
    ]
