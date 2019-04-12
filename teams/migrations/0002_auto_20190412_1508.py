# Generated by Django 2.1.4 on 2019-04-12 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='email',
            field=models.EmailField(default=123, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teams',
            name='image',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='teams',
            name='mate1',
            field=models.CharField(default='队员1', max_length=20),
        ),
        migrations.AddField(
            model_name='teams',
            name='mate2',
            field=models.CharField(default='队员2', max_length=20),
        ),
        migrations.AddField(
            model_name='teams',
            name='mate3',
            field=models.CharField(default='队员3', max_length=20),
        ),
        migrations.AddField(
            model_name='teams',
            name='mate4',
            field=models.CharField(default='队员4', max_length=20),
        ),
        migrations.AddField(
            model_name='teams',
            name='mate5',
            field=models.CharField(default='队员5', max_length=20),
        ),
        migrations.AddField(
            model_name='teams',
            name='name',
            field=models.CharField(default='队伍名', max_length=10),
        ),
        migrations.AlterField(
            model_name='teams',
            name='description',
            field=models.CharField(default='在这里写队伍简介', max_length=100),
        ),
    ]