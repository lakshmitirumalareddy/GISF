# Generated by Django 2.2.5 on 2019-11-01 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UnderWriter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='XxgenInsuredAddress',
            fields=[
                ('insured_addr_id', models.IntegerField(primary_key=True, serialize=False)),
                ('address_Type', models.CharField(blank=True, max_length=20, null=True)),
                ('insured_addr', models.CharField(blank=True, max_length=200, null=True)),
                ('insured_city', models.CharField(blank=True, max_length=200, null=True)),
                ('insured_state', models.CharField(blank=True, max_length=200, null=True)),
                ('insured_country', models.CharField(blank=True, max_length=200, null=True)),
                ('insured_pincode', models.CharField(blank=True, max_length=200, null=True)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateField(blank=True, null=True)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=200, null=True)),
                ('insured_id', models.ForeignKey(blank=True, db_column='insured_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='UnderWriter.XxgenInsuredDtls')),
            ],
        ),
    ]
