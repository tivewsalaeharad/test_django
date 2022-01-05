from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers


from .models import Locality


def showlist(request):
    results = Locality.objects.all
    return render(request, "home.html", {"showcity": results})


class LocalitySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=120)
    url = serializers.CharField()
    population = serializers.IntegerField()


class LocalitiesView(APIView):
    def get(self, request):
        pk = self.request.query_params.get('id')
        localities = Locality.objects.filter(pk=pk)
        serializer = LocalitySerializer(localities, many=True)

        data = serializer.data
        if len(data) > 0:
            return Response(data[0])
        else:
            return Response([])
