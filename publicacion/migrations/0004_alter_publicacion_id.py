# Generated by Django 4.0 on 2021-12-16 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0003_alter_publicacion_fechacreacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]