from django.urls import path
from .views import PlotDetail

urlpatterns = [
    path('farmer/<int:farmer_pk>/plots/<int:plot_id>/', PlotDetail.as_view(), name='plot_detail'),
]
