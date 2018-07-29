# Generated by Django 2.0.7 on 2018-07-24 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainpage', '0006_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('images', models.ImageField(upload_to='product/<django.db.models.fields.CharField>')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Category')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Section')),
                ('sex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainpage.Sex')),
            ],
        ),
    ]