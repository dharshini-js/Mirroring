from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from devices.serializers import DeviceSerializer
from devices.models import device


@csrf_exempt
def DevicesApi(request, id=0):
    if request.method == 'GET':
        get_devices = device.objects.all()
        devices_serializer = DeviceSerializer(get_devices, many=True)
        return JsonResponse(devices_serializer.data, safe=False)
        
    elif request.method == 'POST':
       
        devices_data = JSONParser().parse(request)
        required_fields = ['device_name', 'device_type', 'device_model', 'created_by', 'updated_by']
        missing_fields = [field for field in required_fields if field not in devices_data or not devices_data[field]]

        if missing_fields:
            return JsonResponse(
                {'error': f'Missing or empty fields: {", ".join(missing_fields)}'},
                status=400
            )

        existing_device = device.objects.filter(
            device_name=devices_data['device_name'],
            device_type=devices_data['device_type'],
            device_model=devices_data['device_model']
        ).first()

        if existing_device:
              return JsonResponse(
                {'error': 'The device is already exists.'},
                status=400
            )


        devices_serializer = DeviceSerializer(data=devices_data)

        if devices_serializer.is_valid():
            devices_serializer.save()
            return JsonResponse(devices_serializer.data, status=201)
        else:
            return JsonResponse(devices_serializer.errors, status=400)
