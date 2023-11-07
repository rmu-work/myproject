from django.db import models


class FinancialDocumentTypes(models.Model):
    name = models.CharField(max_length=256, verbose_name='Document Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.name


class Qualifications(models.Model):
    name = models.CharField(max_length=50, verbose_name='Qualification')
    description = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.name


class ELRCertificates(models.Model):
    name = models.CharField(max_length=50, verbose_name='Certificate Name')
    total_subjects = models.IntegerField(null=True, verbose_name='No of Subjects')
    mark_out_of = models.IntegerField(null=True, verbose_name='Total Marks')

    def __str__(self):
        return self.name
