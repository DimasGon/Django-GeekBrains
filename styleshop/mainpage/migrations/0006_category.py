# Generated by Django 2.0.7 on 2018-07-23 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0005_auto_20180723_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Section')),
                ('sex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Sex')),
            ],
        ),
    ]