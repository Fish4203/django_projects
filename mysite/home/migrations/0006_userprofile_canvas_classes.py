# Generated by Django 3.0.5 on 2020-05-04 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compvas', '0003_cachsites'),
        ('home', '0005_auto_20200503_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='canvas_classes',
            field=models.ManyToManyField(to='compvas.CachSites'),
        ),
    ]
