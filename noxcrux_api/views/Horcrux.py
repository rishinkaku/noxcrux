from rest_framework import permissions, status
from noxcrux_api.serializers.Horcrux import HorcruxSerializer
from noxcrux_api.models.Horcrux import Horcrux
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class HorcruxList(APIView):
    """
    List all horcruxes, or create a new horcrux
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        horcruxes = Horcrux.objects.filter(owner=request.user)
        serializer = HorcruxSerializer(horcruxes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HorcruxSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HorcruxDetail(APIView):
    """
    Retrieve, update or delete a horcrux instance
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, name, owner):
        try:
            return Horcrux.objects.get(name=name, owner=owner)
        except Horcrux.DoesNotExist:
            raise Http404

    def get(self, request, name):
        horcrux = self.get_object(name, request.user)
        serializer = HorcruxSerializer(horcrux)
        return Response(serializer.data)

    def put(self, request, name):
        horcrux = self.get_object(name, request.user)
        serializer = HorcruxSerializer(horcrux, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name):
        horcrux = self.get_object(name, request.user)
        horcrux.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
