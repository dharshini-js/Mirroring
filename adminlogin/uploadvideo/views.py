from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Media
from .serializers import MediaSerializer

@api_view(['GET', 'POST','DELETE'])
def upload(request):
    if request.method == 'GET':
        media = Media.objects.all()
        serializer = MediaSerializer(media, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
       
        photo_url = request.data.get('photo_url')  
        if Media.objects.filter(photo_url=photo_url).exists():  
            return Response("This link already exists.", status=status.HTTP_400_BAD_REQUEST)
        serializer = MediaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        media_id = request.data.get('id')  

        if media_id is None:
            return Response({"detail": "ID not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            media = Media.objects.get(id=media_id)  
            media.delete() 
            return Response({"detail": "Media entry deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Media.DoesNotExist:
            return Response({"detail": "Media not found."}, status=status.HTTP_404_NOT_FOUND)
