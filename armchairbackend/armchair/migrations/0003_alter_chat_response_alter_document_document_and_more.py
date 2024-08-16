# Generated by Django 5.1 on 2024-08-12 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('armchair', '0002_alter_chat_user_alter_document_user_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='response',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='processing/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='summary',
            field=models.TextField(blank=True),
        ),
    ]