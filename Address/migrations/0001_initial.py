# Generated by Django 4.1.5 on 2023-02-15 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area_Code', models.CharField(max_length=256)),
                ('City', models.CharField(max_length=256)),
                ('State', models.CharField(max_length=256)),
                ('Category', models.CharField(max_length=256)),
                ('District', models.CharField(max_length=256)),
                ('Sub_registrar_office', models.CharField(max_length=256)),
                ('Village', models.CharField(max_length=256)),
                ('Ward_no', models.CharField(max_length=256)),
                ('Total_extend', models.CharField(max_length=256)),
                ('Extend_of_land', models.CharField(max_length=256)),
                ('Street_name', models.CharField(max_length=256)),
                ('Door_no', models.CharField(max_length=256)),
                ('House_no', models.CharField(max_length=256)),
                ('Dimension', models.CharField(max_length=256)),
                ('Metadata', models.CharField(max_length=256)),
                ('In_marketplace', models.BooleanField(default=False)),
                ('Admin_incharge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admincharge', to=settings.AUTH_USER_MODEL)),
                ('Owned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ownedby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
