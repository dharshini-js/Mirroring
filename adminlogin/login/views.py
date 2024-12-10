from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from login.serializers import LoginSerializer
from login.models import login

@csrf_exempt
def adminLoginApi(request, id=0):
    if request.method == 'GET':
        admin = login.objects.all()
        admin_serializer = LoginSerializer(admin, many=True)
        return JsonResponse(admin_serializer.data, safe=False)
        
    elif request.method == 'POST':
        admin_data = JSONParser().parse(request)
        username = admin_data.get('username')
        password = admin_data.get('password')

        if not username or not password:
            return JsonResponse({"message": "Username and password are required"}, status=400)

        user = login.objects.filter(username=username).first()
        if user is None:
            admin_serializer = LoginSerializer(data=admin_data)
            if admin_serializer.is_valid():
                admin_serializer.save()
                return JsonResponse({"message": "Admin registered successfully"}, status=200)
            return JsonResponse({"message": "Failed to register admin"}, status=400)

        if user.password != password:
            return JsonResponse({"message": "Invalid username or password"}, status=400)

        return JsonResponse({"message": "Login successful"}, status=200)
