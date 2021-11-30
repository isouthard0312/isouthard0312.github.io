# Generated by Django 3.2.9 on 2021-11-21 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='art',
            field=models.ImageField(blank=True, upload_to='social/'),
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='art', max_length=200),
            preserve_default=False,
        ),
    ]
