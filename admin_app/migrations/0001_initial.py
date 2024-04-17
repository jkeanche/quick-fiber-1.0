# Generated by Django 5.0.4 on 2024-04-15 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.TextField()),
                ('contact', models.TextField()),
            ],
            options={
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Finances',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('acc', models.TextField()),
                ('moneyIn', models.IntegerField(db_column='money in')),
                ('moneyOut', models.IntegerField(db_column='money out')),
                ('description', models.TextField()),
                ('date', models.TextField()),
            ],
            options={
                'db_table': 'finance',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.TextField()),
                ('date', models.TextField()),
                ('time', models.TextField()),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'logs',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sender', models.TextField()),
                ('to', models.TextField()),
                ('dateTime', models.TextField()),
                ('message', models.TextField()),
                ('read', models.BooleanField()),
            ],
            options={
                'db_table': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('topic', models.TextField()),
                ('category', models.TextField()),
                ('to', models.TextField()),
                ('dateTime', models.TextField()),
                ('notification', models.TextField()),
                ('read', models.BooleanField()),
            ],
            options={
                'db_table': 'notifications',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('acc', models.TextField()),
                ('code', models.TextField()),
                ('amount', models.IntegerField()),
                ('source', models.TextField()),
                ('date', models.TextField()),
                ('time', models.TextField()),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        migrations.CreateModel(
            name='Pkgs',
            fields=[
                ('pno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('speed', models.IntegerField()),
                ('days', models.IntegerField()),
                ('max_users', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('pkg_type', models.TextField(db_column='type')),
            ],
            options={
                'db_table': 'packages',
            },
        ),
        migrations.CreateModel(
            name='pppoe',
            fields=[
                ('acc', models.TextField(primary_key=True, serialize=False)),
                ('phone', models.TextField()),
                ('location', models.TextField()),
                ('ip', models.TextField()),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('install_date', models.TextField(db_column='install date')),
                ('name', models.TextField()),
                ('package', models.IntegerField()),
                ('balance', models.IntegerField()),
            ],
            options={
                'db_table': 'pppoeAccounts',
            },
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('acc', models.TextField()),
                ('profile', models.TextField()),
                ('startDate', models.TextField(db_column='start date')),
                ('startTime', models.TextField(db_column='start time')),
                ('endDate', models.TextField(db_column='end date')),
                ('endTime', models.TextField(db_column='end time')),
                ('status', models.TextField()),
                ('creation_date', models.TextField(db_column='creation date')),
            ],
            options={
                'db_table': 'sessions',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('acc', models.TextField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('phone', models.TextField()),
                ('package', models.IntegerField()),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('install_date', models.TextField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'hotspotAccounts',
            },
        ),
    ]
