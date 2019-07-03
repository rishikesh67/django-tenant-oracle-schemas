from django.urls import re_path
from . import views


app_name = 'tenants'

urlpatterns = [
	re_path('', views.TenantRegister.as_view(), name='register')
]