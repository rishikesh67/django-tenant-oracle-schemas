from django.db import models
from tenants.models import TenantModel

class User(TenantModel):
	fullname = models.CharField(max_length=50, help_text='Full name')
	age = models.PositiveIntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.fullname + ' ~ ' + str(self.age)
