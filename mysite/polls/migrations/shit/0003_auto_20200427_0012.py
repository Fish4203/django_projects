# Generated by Django 3.0.5 on 2020-04-27 00:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import polls.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0002_question_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(default=polls.models.get_default, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
