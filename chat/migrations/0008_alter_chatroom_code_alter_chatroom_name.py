# Generated by Django 4.2.13 on 2024-07-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_chatroom_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='code',
            field=models.CharField(editable=False, max_length=6, unique=True),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]