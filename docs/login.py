import requests
import json

body = {"appln_id": "TEST854", "password": "test$147", "arn_code": "ARN-70209"}

response = requests.post("http://52.66.245.185:8001/users/auth/login/", json=body)

print(response)

print(response.status_code)

if response.status_code == 200:
	jdata = response.json()
	print(json.dumps(jdata,indent=4))
else:
	print(response)


# {
#     "code": "F1tH2UADOg3pWMbFd5OaMz4Wy0LoPC83",
#     "status": 400,
#     "message": "Already loged in please log off and try again"
# }

# <Response [200]>
# 200
# {
#     "status": 400,
#     "message": "Oops some internal Exception, While processing UserLoginSession"
# }
# (venv3.6.7) ➜  docs git:(master) ✗ 
# (venv3.6.7) ➜  docs git:(master) ✗ python3 login.py
# <Response [200]>
# 200
# {
#     "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5uc2VpbmRpYS5pbiIsImFybl9jb2RlIjoiQVJOLTcwMjA5IiwiYXBwbG5faWQiOiJURVNUODU0IiwibnNlX2FwaV9yZXNwb25zZSI6eyJTZXNzaW9uSUQiOiJNRlN8VEVTVDg1NE5NRklJU0VTU0lPTlZBTElEQVRFQVBJMDM1NzQ0NTc2ODc1NiIsIlN0YXR1cyI6IlN1Y2Nlc3MiLCJFcnJvcl9jb2RlIjoiMDAiLCJEYXRlVGltZSI6IjI2MDYyMDE5MTU0NDU4In19.U5Qj7oiW4Xz1J37TiRgBbqZxA4u_ka7nS07F4a2_KbE",
#     "refreshToken": "RWJLXZJHNEY3MFNUN2FRX3U0QXHACWJCZ1JPVDCZSJF6WDRXAW83ALE1VQ^@|@$eyJpc3MiOiAiaHR0cHM6Ly93d3cubnNlaW5kaWEuaW4iLCAiYXJuX2NvZGUiOiAiQVJOLTcwMjA5IiwgImFwcGxuX2lkIjogIlRFU1Q4NTQiLCAibnNlX2FwaV9yZXNwb25zZSI6IHsiU2Vzc2lvbklEIjogIk1GU3xURVNUODU0Tk1GSUlTRVNTSU9OVkFMSURBVEVBUEkwMzU3NDQ1NzY4NzU2IiwgIlN0YXR1cyI6ICJTdWNjZXNzIiwgIkVycm9yX2NvZGUiOiAiMDAiLCAiRGF0ZVRpbWUiOiAiMjYwNjIwMTkxNTQ0NTgifX0=",
#     "status": 200,
#     "message": "Successfully logged in"
# }