# Generated by Django 2.2.24 on 2022-09-01 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_auto_20220901_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст жалобы')),
                ('flat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to='property.Flat', verbose_name='Квартира')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints', to=settings.AUTH_USER_MODEL, verbose_name='Кто жаловался')),
            ],
        ),
    ]
