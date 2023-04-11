# Generated by Django 4.1.5 on 2023-02-15 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=256)),
                ('status', models.CharField(choices=[('INITIATED', 'INITIATED'), ('APPROVED', 'APPROVED'), ('DENIED', 'DENIED'), ('COMPLETED', 'COMPLETED')], default='INITIATED', max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('reciever', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reciever', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]