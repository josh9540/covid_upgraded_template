# Generated by Django 3.0.4 on 2020-03-27 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200325_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
