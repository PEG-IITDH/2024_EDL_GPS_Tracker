# Generated by Django 4.2.8 on 2024-02-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='buslocation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]