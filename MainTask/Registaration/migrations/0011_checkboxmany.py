# Generated by Django 4.0.6 on 2022-11-16 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registaration', '0010_alter_employeecrud_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkboxmany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boxname_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topic_boxname_id', to='Registaration.checkbox')),
                ('hobbies_id', models.ManyToManyField(to='Registaration.checkbox')),
            ],
        ),
    ]
