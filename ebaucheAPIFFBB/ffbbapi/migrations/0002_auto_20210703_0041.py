# Generated by Django 3.2 on 2021-07-02 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffbbapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]