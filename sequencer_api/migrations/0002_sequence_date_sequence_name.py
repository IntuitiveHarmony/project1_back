# Generated by Django 4.1.1 on 2022-09-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequencer_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequence',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='sequence',
            name='name',
            field=models.CharField(max_length=32, null=True),
        ),
    ]