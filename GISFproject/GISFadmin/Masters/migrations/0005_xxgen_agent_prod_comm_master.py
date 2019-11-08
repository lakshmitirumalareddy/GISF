# Generated by Django 2.2.5 on 2019-10-25 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Masters', '0004_xxgenagenmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xxgen_agent_Prod_Comm_Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comm_percent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_by', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateField(blank=True, null=True)),
                ('last_updated_by', models.CharField(blank=True, max_length=200, null=True)),
                ('last_update_date', models.DateField(blank=True, null=True)),
                ('agen_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Masters.XxgenAgenMaster')),
                ('prod_code', models.ForeignKey(blank=True, db_column='prod_code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Masters.XxgenProductMaster')),
            ],
        ),
    ]
