from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from login.models import login

@csrf_exempt
def adminLoginApi(request):
    if request.method == 'POST':
        admin_data = JSONParser().parse(request)
        email = admin_data.get('email')
        password = admin_data.get('password')

        if not email or not password:
            return JsonResponse(
                {"status": False, "data": {}, "message": "Email and password are required"},
                status=400
            )
        user = login.objects.filter(email=email).first()

        if user is None:
            return JsonResponse(
                {"status": False, "data": {}, "message": "Email does not exist"},
                status=404
            )
        if user.password != password:
            return JsonResponse(
                {"status": False, "data": {}, "message": "Invalid email or password"},
                status=400
            )

        user_data = {
            "id": user.id,
            "name": user.username,
            "email": user.email,
            "password": user.password,
            "updated": user.updated_at,
            "created": user.created_at
        }
        return JsonResponse(
            {"status": True, "data": user_data, "message": "Login successful"},
            status=200
        )

    return JsonResponse(
        {"status": False, "message": "Invalid request method"},
        status=405
    )