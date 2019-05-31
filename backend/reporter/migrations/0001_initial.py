# Generated by Django 2.2.1 on 2019-05-30 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('django_celery_beat', '0011_auto_20190508_0153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('watchman_group_id', models.CharField(max_length=100, null=True, unique=True)),
                ('repairshopr_id', models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('date_generated', models.DateField(auto_now_add=True)),
                ('num_mac_os', models.IntegerField(default=0)),
                ('num_windows_os', models.IntegerField(default=0)),
                ('num_linux_os', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporter.Customer')),
            ],
            options={
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='WatchmanComputer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('os_type', models.CharField(max_length=7)),
                ('os_version', models.CharField(max_length=100)),
                ('ram_gb', models.FloatField()),
                ('hdd_capacity_gb', models.FloatField()),
                ('hdd_usage_gb', models.FloatField()),
                ('computer_id', models.CharField(max_length=100, unique=True)),
                ('date_reported', models.DateField(auto_now_add=True)),
                ('date_last_reported', models.DateField(auto_now_add=True)),
                ('watchman_group_id', models.ForeignKey(db_column='watchman_group_id', on_delete=django.db.models.deletion.CASCADE, to='reporter.Customer', to_field='watchman_group_id')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='WatchmanWarning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warning_id', models.CharField(max_length=100)),
                ('date_reported', models.DateField(auto_now_add=True)),
                ('date_last_checked', models.DateField(auto_now_add=True)),
                ('date_resolved', models.DateField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('computer_id', models.ForeignKey(db_column='computer_id', on_delete=django.db.models.deletion.CASCADE, to='reporter.WatchmanComputer', to_field='computer_id')),
                ('watchman_group_id', models.ForeignKey(db_column='watchman_group_id', on_delete=django.db.models.deletion.CASCADE, to='reporter.Customer', to_field='watchman_group_id')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='SubReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('num_warnings_unresolved_start', models.IntegerField(default=0)),
                ('num_warnings_unresolved_end', models.IntegerField(default=0)),
                ('num_warnings_created', models.IntegerField(default=0)),
                ('num_warnings_resolved', models.IntegerField(default=0)),
                ('num_tickets_created', models.IntegerField(default=0)),
                ('num_tickets_resolved', models.IntegerField(default=0)),
                ('report', models.ForeignKey(db_column='report_id', on_delete=django.db.models.deletion.CASCADE, to='reporter.Report')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='ServiceSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.CharField(max_length=25)),
                ('customer', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='reporter.Customer')),
                ('periodic_task', models.OneToOneField(db_column='periodic_task_id', on_delete=django.db.models.deletion.CASCADE, to='django_celery_beat.PeriodicTask')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ComputerReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('os_type', models.CharField(max_length=7)),
                ('os_version', models.CharField(max_length=100)),
                ('ram_gb', models.FloatField()),
                ('hdd_capacity_gb', models.FloatField()),
                ('hdd_usage_gb', models.FloatField()),
                ('computer', models.ForeignKey(db_column='computer_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='reporter.WatchmanComputer')),
                ('report', models.ForeignKey(db_column='report_id', on_delete=django.db.models.deletion.CASCADE, to='reporter.Report')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
