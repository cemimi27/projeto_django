# Generated by Django 4.2.4 on 2023-09-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_usuario_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo',
            field=models.CharField(choices=[('Administrador', 'ADM'), ('Cliente', 'CLI'), ('Funcionário', 'FUN')], default='Cliente', max_length=50),
        ),
    ]