from django.urls import path
from .views import PlotDetail

urlpatterns = [
    path('farmer/<int:farmer_id>/plots/', PlotDetail.as_view(), name='farmer-plots'),
]
