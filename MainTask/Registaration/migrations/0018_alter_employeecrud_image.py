# Generated by Django 4.0.6 on 2022-11-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registaration', '0017_remove_employeecrud_checkbox_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecrud',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/', verbose_name='photo'),
        ),
    ]