# Generated by Django 4.1.1 on 2022-10-08 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]