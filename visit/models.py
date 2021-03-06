from django.db import models

# Create your models here.
class VisitOccurrence(models.Model):
    visit_occurrence_id = models.BigIntegerField(primary_key=True)
    person_id = models.BigIntegerField(blank=True, null=True)
    visit_concept_id = models.IntegerField(blank=True, null=True)
    visit_start_date = models.DateField(blank=True, null=True)
    visit_start_datetime = models.DateTimeField(blank=True, null=True)
    visit_end_date = models.DateField(blank=True, null=True)
    visit_end_datetime = models.DateTimeField(blank=True, null=True)
    visit_type_concept_id = models.IntegerField(blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.BigIntegerField(blank=True, null=True)
    visit_source_value = models.CharField(max_length=50, blank=True, null=True)
    visit_source_concept_id = models.IntegerField(blank=True, null=True)
    admitted_from_concept_id = models.IntegerField(blank=True, null=True)
    admitted_from_source_value = models.CharField(max_length=50, blank=True, null=True)
    discharge_to_source_value = models.CharField(max_length=50, blank=True, null=True)
    discharge_to_concept_id = models.IntegerField(blank=True, null=True)
    preceding_visit_occurrence_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit_occurrence'


