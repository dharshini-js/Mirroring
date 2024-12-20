from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Store_media

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([AllowAny])
def store_ads(request):
    if request.method == 'GET':
        media = Store_media.objects.all()
        media_list = []
        
        for entry in media:
            data = {
                "id": entry.id,
                "photo_urls": entry.photo_urls.split(',') if entry.photo_urls else [],
                "video_urls": entry.video_urls.split(',') if entry.video_urls else [],
                "count": entry.count, 
                "created_at": entry.created_at,
                "updated_at": entry.updated_at,
            }
            media_list.append(data)
        
        return Response(media_list)

    elif request.method == 'POST':
        photo_urls = request.data.get('photo_urls')
        video_urls = request.data.get('video_urls')
        count = request.data.get('count', 0)  

        if not isinstance(photo_urls, list):
            return Response({"detail": "photo_urls must be a list of URLs."}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(video_urls, list):
            return Response({"detail": "video_urls must be a list of URLs."}, status=status.HTTP_400_BAD_REQUEST)

        if not isinstance(count, int) or count < 0:
            return Response({"detail": "count must be a non-negative integer."}, status=status.HTTP_400_BAD_REQUEST)

        photo_url_str = ','.join(photo_urls)
        video_url_str = ','.join(video_urls)

        media = Store_media.objects.create(photo_urls=photo_url_str, video_urls=video_url_str, count=count)

        response_data = {
            "id": media.id,
            "photo_urls": photo_urls,
            "video_urls": video_urls,
            "count": media.count,
            "created_at": media.created_at,
            "updated_at": media.updated_at,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)

    elif request.method == 'PUT':
        media_id = request.data.get('id')
        photo_urls = request.data.get('photo_urls')
        video_urls = request.data.get('video_urls')
        count = request.data.get('count')

        if not media_id:
            return Response({"detail": "ID not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            media = Store_media.objects.get(id=media_id)

            if photo_urls is not None:
                if not isinstance(photo_urls, list):
                    return Response({"detail": "photo_urls must be a list of URLs."}, status=status.HTTP_400_BAD_REQUEST)
                media.photo_urls = ','.join(photo_urls)

            if video_urls is not None:
                if not isinstance(video_urls, list):
                    return Response({"detail": "video_urls must be a list of URLs."}, status=status.HTTP_400_BAD_REQUEST)
                media.video_urls = ','.join(video_urls)

            if count is not None:
                if not isinstance(count, int) or count < 0:
                    return Response({"detail": "count must be a non-negative integer."}, status=status.HTTP_400_BAD_REQUEST)
                media.count = count

            media.save()

            response_data = {
                "id": media.id,
                "photo_urls": media.photo_urls.split(',') if media.photo_urls else [],
                "video_urls": media.video_urls.split(',') if media.video_urls else [],
                "count": media.count,  
                "created_at": media.created_at,
                "updated_at": media.updated_at,
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except Store_media.DoesNotExist:
            return Response({"detail": "Media not found."}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        media_id = request.data.get('id')

        if not media_id:
            return Response({"detail": "ID not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            media = Store_media.objects.get(id=media_id)
            media.delete()
            return Response({"detail": "Media entry deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Store_media.DoesNotExist:
            return Response({"detail": "Media not found."}, status=status.HTTP_404_NOT_FOUND)
