# Generated by Django 4.1.5 on 2023-02-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("note", "0002_alter_notice_card_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notice",
            name="card_img",
            field=models.ImageField(blank=True, upload_to="card_imgs"),
        ),
    ]