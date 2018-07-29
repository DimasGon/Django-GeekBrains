# Generated by Django 2.0.7 on 2018-07-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_auto_20180723_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='brands/')),
            ],
        ),
        migrations.AlterField(
            model_name='section',
            name='image',
            field=models.ImageField(upload_to='sections/'),
        ),
    ]