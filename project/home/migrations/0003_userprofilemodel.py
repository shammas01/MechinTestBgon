# Generated by Django 4.2.6 on 2023-10-30 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_usermodel_options_alter_usermodel_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ImageField(upload_to='project/profile')),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
