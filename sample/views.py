from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from sample.models import Person, FreeAgent, PackersPlayer
from sample.serializers import PersonSerializer, PackersPlayerSerializer, FreeAgentSerializer

class PersonListCreateAPIView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class FreeAgentListCreateAPIView(ListCreateAPIView):
    queryset = FreeAgent.objects.all()
    serializer_class = PersonSerializer

class FreeAgentDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FreeAgent.objects.all()
    serializer_class = PersonSerializer

class PackersPlayerListCreateAPIView(ListCreateAPIView):
    queryset = PackersPlayer.objects.all()
    serializer_class = PersonSerializer

class PackersPlayerDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PackersPlayer.objects.all()
    serializer_class = PersonSerializer
