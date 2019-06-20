# Generated by Django 2.2.2 on 2019-06-20 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tenant_name',
            field=models.ForeignKey(help_text='Tenant name (FK)', on_delete=django.db.models.deletion.CASCADE, to='tenants.Tenant'),
        ),
    ]
