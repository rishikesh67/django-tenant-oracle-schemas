from django.urls import re_path
from . import views as users_views 

app_name = "users"

urlpatterns = [
	re_path(r'^register$', users_views.UsersView.as_view(), name='users-register'),
	re_path(r"^$", users_views.UsersView.as_view(), name='users-list'),
	re_path(r"^select/tenant$", users_views.TenantSelect.as_view(), name='tenant-select'),
]
