# Generated by Django 4.2.6 on 2023-10-28 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0009_area_city_areafarmsgroup_area_city_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='area_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backendapp.area'),
            preserve_default=False,
        ),
    ]
