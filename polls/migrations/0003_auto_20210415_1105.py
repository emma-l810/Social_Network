# Generated by Django 3.1.6 on 2021-04-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_post_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default='2021-04-15 11:05'),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default='2021-04-15 11:05'),
        ),
    ]
