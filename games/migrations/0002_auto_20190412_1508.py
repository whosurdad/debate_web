# Generated by Django 2.1.4 on 2019-04-12 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='games',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='games',
            name='email',
            field=models.EmailField(default=123, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='games',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='games',
            name='name',
            field=models.CharField(default='比赛名', max_length=10),
        ),
        migrations.AddField(
            model_name='games',
            name='team1',
            field=models.CharField(default='队伍1', max_length=20),
        ),
        migrations.AddField(
            model_name='games',
            name='team2',
            field=models.CharField(default='队伍2', max_length=20),
        ),
        migrations.AlterField(
            model_name='games',
            name='description',
            field=models.CharField(default='在这里写比赛简介', max_length=100),
        ),
    ]