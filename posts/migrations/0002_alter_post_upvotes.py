# Generated by Django 3.2.9 on 2021-12-03 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="upvotes",
            field=models.IntegerField(blank=True, default="0"),
        ),
    ]
