# Generated by Django 3.1.2 on 2020-11-17 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('todo', '0006_auto_20201117_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.client')),
            ],
        ),
    ]
