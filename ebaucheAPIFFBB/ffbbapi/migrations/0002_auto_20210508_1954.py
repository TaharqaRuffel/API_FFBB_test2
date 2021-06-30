# Generated by Django 3.2 on 2021-05-08 17:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ffbbapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=10)),
                ('fax', models.CharField(max_length=10)),
                ('couleur', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('post_code', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 5', regex='^.{5}$')])),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='match',
            options={},
        ),
        migrations.RemoveField(
            model_name='match',
            name='championship',
        ),
        migrations.RemoveField(
            model_name='match',
            name='created',
        ),
        migrations.RemoveField(
            model_name='match',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='match',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='match',
            name='updated',
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='ffbbapi.club')),
            ],
        ),
        migrations.CreateModel(
            name='Pool',
            fields=[
                ('code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('championship', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pools', to='ffbbapi.championship')),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('correspondent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizer_correspondents', to='ffbbapi.member')),
                ('president', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizer_presidents', to='ffbbapi.member')),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ffbbapi.place'),
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pool', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='days', to='ffbbapi.championship')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clubs_address', to='ffbbapi.place'),
        ),
        migrations.AddField(
            model_name='club',
            name='comite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comite', to='ffbbapi.place'),
        ),
        migrations.AddField(
            model_name='club',
            name='correspondent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clubs_correspondent', to='ffbbapi.member'),
        ),
        migrations.AddField(
            model_name='club',
            name='gym',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clubs_gym', to='ffbbapi.place'),
        ),
        migrations.AddField(
            model_name='club',
            name='ligue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clubs', to='ffbbapi.place'),
        ),
        migrations.AddField(
            model_name='club',
            name='president',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clubs_president', to='ffbbapi.member'),
        ),
        migrations.AddField(
            model_name='championship',
            name='organizedBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='championships', to='ffbbapi.organizer'),
        ),
        migrations.AddField(
            model_name='match',
            name='gym',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='ffbbapi.place'),
        ),
        migrations.AlterField(
            model_name='match',
            name='day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches', to='ffbbapi.championship'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_home', to='ffbbapi.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='visitor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='matches_visitor', to='ffbbapi.team'),
        ),
    ]