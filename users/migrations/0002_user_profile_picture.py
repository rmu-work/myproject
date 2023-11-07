# Generated by Django 4.2.4 on 2023-10-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_picture",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="profile/",
                verbose_name="Profile Picture",
            ),
        ),
    ]