# Generated by Django 4.0.4 on 2022-10-28 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cashbookapp', '0008_cashbook_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('cashbook_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cashbookapp.cashbook')),
            ],
        ),
    ]
