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

class UsersView(APIView):
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
            users = User.objects.filter(tenant_name=request.tenant)
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

        print(request.data)
        
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

        try:
            if True:
            # if clients.exists():
                # client = clients.first()
                # print(client)
                response["data"] = {
                    "scheme": "http", # https/http
                    "tenant": 'cfd',
                    "domain": "nseinvestease",
                    "port": 8000,
                    "extension": "com",
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
            response.set_cookie('token', token, domain='nseinvestease.com')

        return response


    def get(self, request, *args, **kwargs):
        return render(request, "users/login.html", {})

