# Generated by Django 4.1.3 on 2023-06-07 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_alter_settlement_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
