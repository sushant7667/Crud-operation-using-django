# Generated by Django 4.1.3 on 2022-11-15 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registaration', '0008_employeecrud_dateofjoining'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boxname', models.CharField(max_length=50, null=True)),
                ('isactive', models.BooleanField(default=True)),
            ],
        ),
    ]
