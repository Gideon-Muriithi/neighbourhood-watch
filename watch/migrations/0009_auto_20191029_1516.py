# Generated by Django 2.2.6 on 2019-10-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watch', '0008_auto_20191029_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='occupants_count',
            field=models.IntegerField(blank=True),
        ),
    ]