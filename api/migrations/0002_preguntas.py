# Generated by Django 3.2.4 on 2023-10-18 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('id_respuesta', models.AutoField(db_column='id_respuesta', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(db_column='P1', max_length=255)),
                ('descripcion1', models.CharField(db_column='P2', max_length=255)),
                ('descripcion2', models.CharField(db_column='P3', max_length=255)),
                ('descripcion3', models.CharField(db_column='P4', max_length=255)),
                ('descripcion4', models.CharField(db_column='P5', max_length=255)),
                ('descripcion5', models.CharField(db_column='P6', max_length=255)),
                ('descripcion6', models.CharField(db_column='P7', max_length=255)),
                ('descripcion7', models.CharField(db_column='P8', max_length=255)),
                ('descripcion8', models.CharField(db_column='P9', max_length=255)),
                ('descripcion9', models.CharField(db_column='P10', max_length=255)),
                ('descripcion10', models.CharField(db_column='P11', max_length=255)),
            ],
            options={
                'db_table': 'Services',
            },
        ),
    ]
