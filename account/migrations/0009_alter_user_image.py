# Generated by Django 4.1.2 on 2022-10-09 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_alter_user_address_alter_user_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
