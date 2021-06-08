# Generated by Django 3.2.3 on 2021-05-14 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Poll",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tite", models.CharField(max_length=128)),
                ("text", models.TextField(blank=True)),
                ("score", models.IntegerField(default=0)),
            ],
        ),
    ]
