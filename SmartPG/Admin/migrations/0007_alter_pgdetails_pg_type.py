# Generated by Django 4.2.6 on 2023-10-26 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_alter_pgdetails_pg_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pgdetails',
            name='pg_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.pgtype'),
        ),
    ]
