from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def request(self):
	return render(request, 'tests/drop.html', {})

class TenantCreateView(APIView):

	def post(self, request, *args, **kwargs):
		status, message, response = 200, 'Successfully created tenant', {}
		data = request.data

		print(data)
		response['status'] = status
		response['message'] = message
		return Response(response)
	
