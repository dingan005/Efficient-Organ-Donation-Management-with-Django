# Generated by Django 5.0.1 on 2024-02-17 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notif_title', models.CharField(max_length=20)),
                ('notif_details', models.CharField(max_length=20)),
            ],
        ),
    ]
