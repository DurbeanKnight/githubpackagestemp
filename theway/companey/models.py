from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.conf import settings
import os

from minio import Minio
from urllib.parse import urlparse


class Company(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='employee_photos/', null=True, blank=True)
    minio_object_name = models.CharField(max_length=100)  # Store MinIO object name


    def __str__(self):
        return self.name
    


@receiver(pre_delete, sender=Company)
def delete_company_media(sender, instance, **kwargs):
    # Delete the company's logo when the company is deleted
    if instance.logo:
        instance.logo.delete(save=False)

@receiver(pre_delete, sender=Employee)
def delete_employee_media(sender, instance, **kwargs):
    if instance.photo:
        instance.photo.delete(save=False)

# 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

#  echo "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" | docker login ghcr.io -u DurbeanKnight --password-stdin