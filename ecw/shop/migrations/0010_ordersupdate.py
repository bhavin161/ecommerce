# Generated by Django 3.0.7 on 2020-07-11 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20200710_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='', max_length=50)),
                ('update_desc', models.CharField(default='', max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
