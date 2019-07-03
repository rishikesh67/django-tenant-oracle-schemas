from django.urls import re_path
from . import views as this_views

app_name = 'tests'

urlpatterns = [
	re_path(r'^register$', this_views.TenantCreateView.as_view(), name='register'),
]