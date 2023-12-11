# Generated by Django 4.2.7 on 2023-12-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('USER_ID', models.IntegerField(db_column='USER_ID', primary_key=True, serialize=False)),
                ('FIRST_NAME', models.TextField(blank=True, db_column='FIRST_NAME', null=True)),
                ('LAST_NAME', models.TextField(blank=True, db_column='LAST_NAME', null=True)),
                ('PASSWORD', models.TextField(blank=True, db_column='PASSWORD', null=True)),
            ],
            options={
                'db_table': 'USER',
                'managed': False,
            },
        ),
    ]
