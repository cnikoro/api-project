# Generated by Django 3.2.6 on 2021-08-04 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.department')),
            ],
        ),
    ]