# Generated by Django 4.1.1 on 2022-10-25 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default="{% static 'images/spongebob-patrick.gif'%}", null=True, upload_to='profiles/'),
        ),
    ]
