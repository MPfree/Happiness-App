# Generated by Django 3.0.5 on 2020-04-19 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=15)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserHappinessData',
            fields=[
                ('date', models.DateField(primary_key=True, serialize=False)),
                ('sleep', models.FloatField()),
                ('exercise', models.FloatField()),
                ('social', models.FloatField()),
                ('metime', models.FloatField()),
                ('weather', models.FloatField()),
                ('socialmedia', models.FloatField()),
                ('happy', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.UserInformation')),
            ],
        ),
    ]