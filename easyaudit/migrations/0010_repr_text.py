# Generated by Django 2.0.4 on 2018-04-09 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("easyaudit", "0009_auto_20180314_2225"),
    ]

    operations = [
        migrations.AlterField(
            model_name="crudevent",
            name="object_repr",
            field=models.TextField(blank=True, null=True),
        ),
    ]
