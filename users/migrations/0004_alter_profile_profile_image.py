# Generated by Django 4.1.1 on 2022-10-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_profile_tags_delete_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/spongebob-patrick.gif', null=True, upload_to=''),
        ),
    ]
