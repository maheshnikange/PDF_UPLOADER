# Generated by Django 4.2.1 on 2023-05-25 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='demo1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME_OF_NATURAL_GAS_PIPELINE', models.CharField(max_length=30)),
                ('BID_DOCUMENT_NO', models.CharField(max_length=30)),
                ('Tender_Document_Fee', models.CharField(max_length=30)),
            ],
        ),
    ]
