# Generated by Django 3.2.4 on 2021-08-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carga', '0004_op_archivoop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codcli', models.BigAutoField(primary_key=True, serialize=False)),
                ('razsoc', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='op',
            name='archivoop',
            field=models.FileField(blank=True, null=True, upload_to='archivoop', verbose_name='Archivo OP'),
        ),
        migrations.AlterField(
            model_name='op',
            name='deudaop',
            field=models.CharField(choices=[('OK', 'OK'), ('DUDA', 'DUDA')], default='DUDA', max_length=4, verbose_name='Deuda'),
        ),
        migrations.AlterField(
            model_name='op',
            name='estadoop',
            field=models.CharField(choices=[('OK', 'OK'), ('DUDA', 'DUDA')], default='DUDA', max_length=4, verbose_name='Estado OP'),
        ),
        migrations.AlterField(
            model_name='op',
            name='fact',
            field=models.CharField(choices=[('100%', '100%'), ('0%', '0%'), ('50%', '50%')], default='100%', max_length=5, verbose_name='Facturacion %'),
        ),
        migrations.AlterField(
            model_name='op',
            name='observaciones',
            field=models.TextField(blank=True, default=' ', null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='op',
            name='tipoop',
            field=models.CharField(choices=[('Esp/Burb', 'Esp/Burb'), ('Reventa', 'Reventa')], max_length=10, verbose_name='Tipo OP'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='nfactura1',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='N° Factura 1'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='nfactura2',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='N° Factura 2'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='npedido1',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='N° Pedido 1'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='npedido2',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='N° Pedido 2'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='nrecibo1',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='N° Recibo 1'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='nrecibo2',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='N° Recibo 2'),
        ),
        migrations.AlterField(
            model_name='remito',
            name='fecharem2',
            field=models.DateField(blank=True, default='2021-01-01', null=True, verbose_name='Fecha remito 2'),
        ),
        migrations.AlterField(
            model_name='remito',
            name='nrem1',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='N° Remito 1'),
        ),
        migrations.AlterField(
            model_name='remito',
            name='nrem2',
            field=models.IntegerField(blank=True, default='0', null=True, verbose_name='N° Remito 2'),
        ),
    ]
