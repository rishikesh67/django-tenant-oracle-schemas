from rest_framework.views import APIView
from .models import 

class UserLogin(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        response = {}
        status = 400
        
        # clients = Client.objects.filter(schema_name=request.data.get("tenant"))

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
                    "token": jwt.encode({
                        "appName": "NMF",
                        "iss": "http://www.nseinvestease.com",
                        "username": "User347",
                        "userId": "MfUser4321",
                        "isMfUser": True,
                        "browserId": "^BidComplex$",
                        "created": str(datetime.now())
                    }, "^NseSecret@123$", algorithm="HS256")
                }
                # ^Nse+Secret~Money#bloom@123$
                status = 200
                message = "Successfully logged in"  
            else:
                status = 400
                message = "User does not exist"          
        except Exception as error:
            response["message"] = str(error)

        response["status"] = status
        response["message"] = message
        print(response)
        return Response(response)


    def get(self, request, *args, **kwargs):
        return render(request, "users/login.html", {})




