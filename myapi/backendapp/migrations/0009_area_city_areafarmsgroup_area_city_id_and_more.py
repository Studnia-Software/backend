# Generated by Django 4.2.6 on 2023-10-28 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backendapp', '0008_alter_farm_id_alter_post_id_alter_price_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='AreaFarmsGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.area')),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='city_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.city'),
        ),
        migrations.AddField(
            model_name='farm',
            name='farms_group_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backendapp.areafarmsgroup'),
            preserve_default=False,
        ),
    ]