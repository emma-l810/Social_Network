# Generated by Django 3.2.3 on 2021-05-25 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_alter_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentingOn',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.post'),
        ),
    ]
