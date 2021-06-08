# Generated by Django 3.2.3 on 2021-05-26 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.RemoveField(
            model_name="category",
            name="posts",
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ManyToManyField(blank=True, to="blogging.Category"),
        ),
    ]
