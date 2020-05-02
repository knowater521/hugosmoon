# Generated by Django 3.0.2 on 2020-01-18 10:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vmm', '0003_auto_20200117_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='folder',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('folder_name', models.CharField(db_column='folder_name', max_length=255)),
                ('isdelete', models.BooleanField(db_column='is_delete', default=False)),
                ('createtime', models.DateTimeField(db_column='f_createtime', default=django.utils.timezone.now)),
                ('updatetime', models.DateTimeField(db_column='f_updatetime', default=django.utils.timezone.now)),
            ],
        ),
    ]
