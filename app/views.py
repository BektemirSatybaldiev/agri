from rest_framework import generics, permissions
from django.http import HttpRequest
from app.models import Plot
from app.serializers import PlotSerializer
from .permissions import IsFarmer


class PlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes = [permissions.IsAuthenticated, IsFarmer]

    def get_queryset(self):
        return Plot.objects.filter(farmer=self.request.user.farmer)


class PlotCreate(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsFarmer]
    serializer_class = PlotSerializer

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user.farmer)

    def get_queryset(self):
        return Plot.objects.filter(farmer=self.request.user.farmer)
