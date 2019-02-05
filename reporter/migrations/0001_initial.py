# Generated by Django 2.1.5 on 2019-02-05 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('watchman_group_id', models.TextField(null=True, unique=True)),
                ('repairshopr_id', models.TextField(null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WatchmanWarning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_id', models.TextField()),
                ('warning_id', models.TextField()),
                ('date_reported', models.DateField(auto_now_add=True)),
                ('date_last_checked', models.DateField(auto_now_add=True)),
                ('date_resolved', models.DateField(null=True)),
                ('name', models.TextField()),
                ('details', models.TextField()),
                ('watchman_group_id', models.ForeignKey(db_column='watchman_group_id', on_delete=django.db.models.deletion.CASCADE, to='reporter.Customer', to_field='watchman_group_id')),
            ],
        ),
    ]
