from django.db import models
import uuid


class Tenant(models.Model):
	# pk => tenant.Tenant.pk: (fields.E003) 'pk' is a reserved word that cannot be used as a field name.
	id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
	name = models.CharField(max_length=20, null=True, blank=True, help_text='Tenant name', unique=True)
	created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __str__(self):
		return str(self.pk) +  ' ~ ' + self.name.upper()

