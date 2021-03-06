# Generated by Django 3.2.6 on 2021-10-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(default='', max_length=5000)),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('phonenumber', models.IntegerField(default=0)),
                ('address1', models.CharField(default='', max_length=100)),
                ('address2', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=100)),
                ('zip_code', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
