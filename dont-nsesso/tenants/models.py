from django.db import models
import uuid
import logging
# from nsessoracle.utils import get_connection 
# from tests.makemigrations_and_migrate import makemigrations_and_migrate
# import os


logger = logging.getLogger(__name__)

class Tenant(models.Model):
    # pk => tenant.Tenant.pk: (fields.E003) 'pk' is a reserved word that cannot be used as a field name.
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    tenant_name = models.CharField(max_length=20, null=True, blank=True, help_text='Tenant name', unique=True)
    # created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.pk) +  ' ~ ' + self.tenant_name.upper()


    def save(self, *args, **kwargs):
    	self.tenant_name = tenant_name.lower()
    	super().save(*args, **kwargs)


class TenantModel(models.Model):
    tenant_name = models.ForeignKey(Tenant, on_delete=models.CASCADE, help_text='Tenant name (FK)')

    class Meta:
        abstract= True
