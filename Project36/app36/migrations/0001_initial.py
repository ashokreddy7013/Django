# Generated by Django 2.0.7 on 2018-11-23 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeReg',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('contact', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
