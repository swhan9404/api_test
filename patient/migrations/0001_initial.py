# Generated by Django 3.2.5 on 2021-07-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionOccurrence',
            fields=[
                ('condition_occurrence_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('person_id', models.BigIntegerField(blank=True, null=True)),
                ('condition_concept_id', models.IntegerField(blank=True, null=True)),
                ('condition_start_date', models.DateField(blank=True, null=True)),
                ('condition_start_datetime', models.DateTimeField(blank=True, null=True)),
                ('condition_end_date', models.DateField(blank=True, null=True)),
                ('condition_end_datetime', models.DateTimeField(blank=True, null=True)),
                ('condition_type_concept_id', models.IntegerField(blank=True, null=True)),
                ('condition_status_concept_id', models.IntegerField(blank=True, null=True)),
                ('stop_reason', models.CharField(blank=True, max_length=20, null=True)),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_occurrence_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_detail_id', models.BigIntegerField(blank=True, null=True)),
                ('condition_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('condition_source_concept_id', models.IntegerField(blank=True, null=True)),
                ('condition_status_source_value', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'condition_occurrence',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Death',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_id', models.BigIntegerField(blank=True, null=True)),
                ('death_date', models.DateField(blank=True, null=True)),
                ('death_datetime', models.DateTimeField(blank=True, null=True)),
                ('death_type_concept_id', models.IntegerField(blank=True, null=True)),
                ('cause_concept_id', models.BigIntegerField(blank=True, null=True)),
                ('cause_source_value', models.IntegerField(blank=True, null=True)),
                ('cause_source_concept_id', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'death',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DrugExposure',
            fields=[
                ('drug_exposure_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('person_id', models.BigIntegerField(blank=True, null=True)),
                ('drug_concept_id', models.IntegerField(blank=True, null=True)),
                ('drug_exposure_start_date', models.DateField(blank=True, null=True)),
                ('drug_exposure_start_datetime', models.DateTimeField(blank=True, null=True)),
                ('drug_exposure_end_date', models.DateField(blank=True, null=True)),
                ('drug_exposure_end_datetime', models.DateTimeField(blank=True, null=True)),
                ('verbatim_end_date', models.DateField(blank=True, null=True)),
                ('drug_type_concept_id', models.IntegerField(blank=True, null=True)),
                ('stop_reason', models.CharField(blank=True, max_length=20, null=True)),
                ('refills', models.IntegerField(blank=True, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('days_supply', models.IntegerField(blank=True, null=True)),
                ('sig', models.TextField(blank=True, null=True)),
                ('route_concept_id', models.IntegerField(blank=True, null=True)),
                ('lot_number', models.CharField(blank=True, max_length=50, null=True)),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_occurrence_id', models.BigIntegerField(blank=True, null=True)),
                ('visit_detail_id', models.BigIntegerField(blank=True, null=True)),
                ('drug_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('drug_source_concept_id', models.IntegerField(blank=True, null=True)),
                ('route_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('dose_unit_source_value', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'drug_exposure',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('gender_concept_id', models.IntegerField(blank=True, null=True)),
                ('year_of_birth', models.IntegerField(blank=True, null=True)),
                ('month_of_birth', models.IntegerField(blank=True, null=True)),
                ('day_of_birth', models.IntegerField(blank=True, null=True)),
                ('birth_datetime', models.DateTimeField(blank=True, null=True)),
                ('race_concept_id', models.IntegerField(blank=True, null=True)),
                ('ethnicity_concept_id', models.IntegerField(blank=True, null=True)),
                ('location_id', models.BigIntegerField(blank=True, null=True)),
                ('provider_id', models.BigIntegerField(blank=True, null=True)),
                ('care_site_id', models.BigIntegerField(blank=True, null=True)),
                ('person_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('gender_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('gender_source_concept_id', models.IntegerField(blank=True, null=True)),
                ('race_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('race_source_concept_id', models.IntegerField(blank=True, null=True)),
                ('ethnicity_source_value', models.CharField(blank=True, max_length=50, null=True)),
                ('ethnicity_source_concept_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'person',
                'managed': False,
            },
        ),
    ]
