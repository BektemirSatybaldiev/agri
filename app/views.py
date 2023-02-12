from rest_framework import generics, permissions

from app.models import Plot
from app.serializers import PlotSerializer
from .permissions import IsFarmer


class PlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes = [permissions.IsAuthenticated, IsFarmer]


class PlotCreate(generics.ListCreateAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes = [permissions.IsAuthenticated, IsFarmer]

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user.farmer)
