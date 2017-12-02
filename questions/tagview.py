
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Tag
from .serializers import  TagSerializer


class TagView(APIView):
    """
    Tag view specifies options to create tags
    """

    def get(self):
        """
        Responds to get method, returns TagList
        :return: Response
        """
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Save tag to database
        :param request: DRF Request
        :return: Status code
        """
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
