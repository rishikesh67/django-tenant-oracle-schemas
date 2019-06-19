from django.contrib import admin
from users.models import User 


class UserAdmin(admin.ModelAdmin):
	list_display = [
		"pk",
		"id",
		"fullname",
		"age",
		"created_at",
		"updated_at"
	]

admin.site.register(User)