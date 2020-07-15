from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("easyaudit", "0013_auto_20190723_0126"),
    ]

    operations = [
        migrations.AddField(
            model_name="crudevent",
            name="object_id",
            field=models.CharField(max_length=255),
        ),
    ]
