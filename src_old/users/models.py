from django.db import models
from tenants.models import TenantModel


class TenantUsersManager(models.Manager):
	"""
	Now the below statement can be executed from all the views

	> User.tenant_users.filter(username='admin')
	"""
	def get_queryset(self):
		print("Inside Model Manager's Code")
		tenant_users = super().get_queryset().filter(tenant_name=request.tenant)
		return tenant_users


class User(TenantModel):
	fullname = models.CharField(max_length=50, help_text='Full name')
	age = models.PositiveIntegerField(default=0)
	username = models.CharField(max_length=20, unique=True, null=False, blank=True, help_text='Username')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	# tenant_users = TenantUsersManager()

	def __str__(self):
		return self.fullname + ' ~ ' + str(self.age)

	class Meta:
		unique_together = ('username', 'tenant_name')
