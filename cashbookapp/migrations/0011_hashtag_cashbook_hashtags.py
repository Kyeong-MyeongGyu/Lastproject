# Generated by Django 4.0.4 on 2022-11-03 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0010_comment_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='cashbook',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='cashbookapp.hashtag'),
        ),
    ]
