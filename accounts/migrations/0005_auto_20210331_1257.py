# Generated by Django 3.1.7 on 2021-03-31 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
        ('accounts', '0004_auto_20210331_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='College',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.college'),
        ),
    ]
