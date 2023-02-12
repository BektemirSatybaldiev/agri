from django.urls import path
from .views import PlotDetail, PlotCreate

urlpatterns = [
    path('farmer/<int:farmer_pk>/plots/<int:plot_id>/', PlotDetail.as_view(), name='plot_detail'),
    path('farmer/<int:farmer_pk>/plots/add/', PlotCreate.as_view(), name='plot-list'),
]
