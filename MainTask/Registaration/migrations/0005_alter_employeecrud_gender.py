# Generated by Django 4.1.3 on 2022-11-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registaration', '0004_alter_employeecrud_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecrud',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=50),
        ),
    ]
