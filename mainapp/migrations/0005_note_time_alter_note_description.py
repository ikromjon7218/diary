# Generated by Django 4.2 on 2023-05-18 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_daily_bed_time_alter_daily_event_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
