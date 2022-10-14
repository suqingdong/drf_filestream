from pathlib import Path
from django.conf import settings
from rest_framework import permissions, views, status
from rest_framework.response import Response

from .utils import get_response



class FileStreamView(views.APIView):

    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, filepath):
        file = Path(settings.MEDIA_ROOT).joinpath(filepath)

        if not file.exists():
            return Response({'msg': 'file not exists!'}, status=status.HTTP_404_NOT_FOUND)

        return get_response(file, request)
