from django.urls import re_path
from . import views as tests_views

app_name = 'tests'

urlpatterns = [
	re_path(r'^abc/$', tests_views.login, name='tests-login'),
	re_path(r'^tenants/$', tests_views.tenants, name='tests-tenants'),
	re_path(r'^xyz/$', tests_views.logout, name='tests-logout'),
]