# Generated by Django 3.2.9 on 2021-11-10 22:06

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
            name='Fayl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=264)),
                ('fayl', models.FileField(blank=True, null=True, upload_to='documents/%Y/%m/%d')),
                ('aciqlama', models.TextField()),
                ('muellif', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fayllar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Serh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('komment', models.TextField()),
                ('fayl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serhler', to='taskapp.fayl')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serh', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Paylas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serh_yaza_biler', models.BooleanField(default=False)),
                ('fayl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paylasilan_sexsler', to='taskapp.fayl')),
                ('kimle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gore_bildiyi_fayllar', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
