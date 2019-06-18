from django.contrib import admin
from tenants.models import Tenant


class TenantAdmin(admin.ModelAdmin):
	list_display = [
		'pk', # tenant.Tenant.pk: (fields.E003) 'pk' is a reserved word that cannot be used as a field name.
		'id',
		'name',
		'created_at',
		'updated_at'
	]


admin.site.register(Tenant, TenantAdmin)
