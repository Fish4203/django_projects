# Generated by Django 3.0.5 on 2020-04-27 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0005_auto_20200427_0104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='comment_post',
        ),
        migrations.AddField(
            model_name='posts',
            name='comment_link',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='message.Comments'),
        ),
    ]
