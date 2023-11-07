from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()


class Attachments(models.Model):
    student = models.ForeignKey(USER_MODEL, related_name='studentdocument', on_delete=models.SET_NULL, null=True)
    document_type = models.CharField(max_length=125, verbose_name='Document Type')
    document = models.FileField(upload_to='documents/', null=True, verbose_name='Document')
    uploaded_at = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name='Uploaded At')

    def __str__(self):
        return f"{self.student.get_full_name()}'s - Attachments"


class Academics(models.Model):
    student = models.ForeignKey(USER_MODEL, related_name='studentacdmcs', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=256, verbose_name='University/School Name')
    qualification = models.CharField(max_length=100, null=True, verbose_name='Qualification')
    start_date = models.DateField(null=True, verbose_name='Start Date')
    end_date = models.DateField(null=True, verbose_name='End Date')
    grade = models.CharField(max_length=40, blank=True, null=True, verbose_name='Grade / Mark')
    remarks = models.CharField(max_length=512, blank=True, null=True, verbose_name='Remarks')



class EnglishLanguageRequirement(models.Model):
    student = models.ForeignKey(USER_MODEL, related_name='studentelr', on_delete=models.SET_NULL, null=True)
    candidate_id = models.CharField(max_length=125, null=True, verbose_name='Candidate ID')
    expiry_date = models.DateField(null=True, verbose_name='Expiry date')
