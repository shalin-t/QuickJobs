# Generated by Django 4.2.7 on 2023-11-20 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0002_alter_jobposting_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
