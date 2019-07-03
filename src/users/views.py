from django.shortcuts import render
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
import traceback
from rest_framework.views import APIView
from datetime import datetime
import jwt
from django.http import JsonResponse
from tenants.models import Tenant
from django.conf import settings
from nsessoracle.mixins import TenantDataMixin


class UsersView(APIView, TenantDataMixin):
    def post(self, request, *args, **kwargs):
        status, message, response = 400, 'Successfully created user', {}
        data = request.data
        data["tenant_name"] = request.tenant

        print(data)

        try:    
            user = User.objects.filter(username=data["username"])
            if user:
                message = 'User is already registered'
            else:
                user = User.objects.create(**data)
                status = 200
        except KeyError as error:
            message = "Invalid/insufficient body parameters (username, fullname, age)"
        except Exception as error:
            print(error)
            message = str(error)

            traceback.print_tb(error)


        response["status"] = status
        response["message"] = message

        return Response(response)


    def get(self, request, *args, **kwargs):
        status, message, response = 400, 'Successfully fetched users', {}
        data = request.data

        try:
            # users = User.objects.filter(tenant_name=request.tenant)
            users = self.get_data(request, User, many=True) # Mixin's method

            serializer = UserSerializer(users, many=True)
            response["data"] = serializer.data
            status = 200
        except Exception as error:
            message = str(error)

        response["status"] = status
        response["message"] = message

        return Response(response)


class UserLogin(APIView):
    def post(self, request, *args, **kwargs):
        status, message, response = 400, 'Successfully logged in', {}
        data = request.data
        print(data)
        password = data.get('password')
        arn_code = data.get('arn_code')
        appln_id = data.get('appln_id')
        print(password, arn_code, appln_id)
        print('Set tenant')
        # tenant = Tenant.objects.filter(tenant_name=request.tenant).first(tenant_name=request.tenant.tenant_name)

        # if not request.tenant:
        #     return Response({
        #         'status': status,
        #         'message': 'Could not find this tenant'
        #     })
        
        # clients = Client.objects.filter(schema_name=request.data.get("tenant"))
        token = jwt.encode({
                        "appName": "NMF",
                        "iss": "http://www.nseinvestease.com",
                        "username": "User347",
                        "userId": "MfUser4321",
                        "isMfUser": True,
                        "browserId": "^BidComplex$",
                        "created": str(datetime.now())
                    }, "^NseSecret@123$", algorithm="HS256").decode('utf8')

        # token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjE0NjU3MDQsImlzcyI6Imh0dHBzOi8vd3d3Lm5zZWluZGlhLmluIiwiYXJuX2NvZGUiOiJBUk4tNzAyMDkiLCJhcHBsbl9pZCI6IlRFU1Q4NTQiLCJuc2VfYXBpX3Jlc3BvbnNlIjp7IlNlc3Npb25JRCI6Ik1GU3xURVNUODU0Tk1GSUlTRVNTSU9OVkFMSURBVEVBUEkwNTIzNDMyMzI3NjM0IiwiU3RhdHVzIjoiU3VjY2VzcyIsIkVycm9yX2NvZGUiOiIwMCIsIkRhdGVUaW1lIjoiMjUwNjIwMTkxNzQzMjQifX0.Z921u-qYku5f7dUGBmA5uuY8lXAQohEd1P18JI_mZyg"
        # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjE0NjgzMDAsImlzcyI6Imh0dHBzOi8vd3d3Lm5zZWluZGlhLmluIiwiYXJuX2NvZGUiOiJBUk4tNzAyMDkiLCJhcHBsbl9pZCI6IlRFU1Q4NTQiLCJuc2VfYXBpX3Jlc3BvbnNlIjp7IlNlc3Npb25JRCI6Ik1GU3xURVNUODU0Tk1GSUlTRVNTSU9OVkFMSURBVEVBUEkwNjQwMjY0MDM3NDM5IiwiU3RhdHVzIjoiU3VjY2VzcyIsIkVycm9yX2NvZGUiOiIwMCIsIkRhdGVUaW1lIjoiMjUwNjIwMTkxODI2NDAifX0.IoIRdO4MoSBzSaB4oF7AGlfMunVkA4aQ-cpdX4slSIQ'
        
        # 540 (9 hours from 10:20)
        # token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjE1NTcwNDQsImlzcyI6Imh0dHBzOi8vd3d3Lm5zZWluZGlhLmluIiwiYXJuX2NvZGUiOiJBUk4tNzAyMDkiLCJhcHBsbl9pZCI6IlRFU1Q4NTQiLCJuc2VfYXBpX3Jlc3BvbnNlIjp7IlNlc3Npb25JRCI6Ik1GU3xURVNUODU0Tk1GSUlTRVNTSU9OVkFMSURBVEVBUEkxMDQzMjA0MzI2NjY2IiwiU3RhdHVzIjoiU3VjY2VzcyIsIkVycm9yX2NvZGUiOiIwMCIsIkRhdGVUaW1lIjoiMjYwNjIwMTkxMDIwNDMifX0.HHejkGs8TtpuW3HUK1an3aFClrDvqJYQIc1Tzjy81kw'
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjE2NDI4NzAsImlzcyI6Imh0dHBzOi8vd3d3Lm5zZWluZGlhLmluIiwiYXJuX2NvZGUiOiJBUk4tNzAyMDkiLCJhcHBsbl9pZCI6IlRFU1Q4NTQiLCJuc2VfYXBpX3Jlc3BvbnNlIjp7IlNlc3Npb25JRCI6Ik1GU3xURVNUODU0Tk1GSUlTRVNTSU9OVkFMSURBVEVBUEkxMDA5MTE5OTc4MzUiLCJTdGF0dXMiOiJTdWNjZXNzIiwiRXJyb3JfY29kZSI6IjAwIiwiRGF0ZVRpbWUiOiIyNzA2MjAxOTEwMTExMCJ9fQ.C7Lamz8G225rkDsjD4s_chVHn_uaP8XB20L-m49sEfU'

        try:
            if True:
            # if clients.exists():
                # client = clients.first()
                # print(client)
                response["data"] = {
                    "scheme": "http", # https/http
                    "tenant": 'cfd',
                    # "domain": settings.REDIRECT_DOMAIN,
                    # "port": settings.REDIRECT_PORT,
                    # "extension": "com",
                    "token": token
                }
                # ^Nse+Secret~Money#bloom@123$

                status = 200
            else:
                message = "User does not exist"          
        except Exception as error:
            print(error)
            response["message"] = str(error)

        response["status"] = status
        response["message"] = message
        print(response)
        response = JsonResponse(response)

        if status == 200:
            # https://stackoverflow.com/questions/18492576/share-cookie-between-subdomain-and-domain
            print('REDIRECT_DOMAIN ',settings.REDIRECT_DOMAIN)
            domain = '.'+ settings.REDIRECT_DOMAIN
            response.set_cookie('token', token)
            # response.set_cookie('token', token, domain=domain.lstrip('.'))
            print('Set cookie for this domain', domain)

            # response.set_cookie('cfd_tuts', 'cfd@gmail.com', domain='.tutorialspoint.com')
            # response.set_cookie('cfd_tuts', 'cfd@gmail.com', domain='.tutorialspoint.com')
            print('Set cookie for .tutorialspoint')

        return response


    def get(self, request, *args, **kwargs):
        return render(request, "users/login.html", {})



class TenantSelect(APIView):
    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        print('Tenant select screen')
        tenants = Tenant.objects.all()
        port = settings.REDIRECT_PORT
        domain = settings.REDIRECT_DOMAIN

        context = {
            'tenants': tenants,
            'port': port,
            'domain': domain
        }
        print('Tenants ', tenants)

        return render(request, 'tenants/tenant_select.html', context)   


class UserRegister(APIView):
    def post(self, request, *args, **kwargs):
        message = 'Successfully registered'
        status = 400
        response = {}
        data = request.data
        print(data) # {'email': 'cfd@gmail.com', 'password': 'test$147', 'tenant_name': 'cfd', 'contact': '7975797484'}

        tenant_name = data.get('tenant_name')
        tenant = Tenant.objects.filter(tenant_name=tenant_name).first()

        try:
            if tenant:
                message = "Tenant is already registered"
            else:
                tenant = Tenant.objects.create(tenant_name=tenant_name)
                response['data'] = {
                    'id': tenant.pk,
                    'tenant_name': tenant.tenant_name
                }
                status = 200 # SUCCESS
        except Exception as error:
            message = str(error)

        response['status'] = status
        response['message'] = message
        return Response(response)

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'tenants/register.html', context)
