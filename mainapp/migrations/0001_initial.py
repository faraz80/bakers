# Generated by Django 3.1.12 on 2022-08-31 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('section', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('elementid', models.AutoField(primary_key=True, serialize=False)),
                ('name_grms', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.CharField(max_length=100)),
                ('typee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.tags')),
            ],
        ),
    ]
