from rest_framework import generics

from app.models import Plot
from app.serializers import PlotSerializer
from .permissions import IsOwner


class PlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plot.objects.all()
    serializer_class = PlotSerializer
    permission_classes = (IsOwner,)
