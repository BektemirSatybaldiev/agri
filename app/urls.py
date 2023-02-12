from django.urls import path
from .views import PlotDetail, PlotCreate

urlpatterns = [
    path('farmer/plots/<int:pk>/', PlotDetail.as_view(), name='plot_detail'),
    path('farmer/plots/add/', PlotCreate.as_view(), name='plot-list'),
    path('farmer/plots/', PlotDetail.as_view(), name='plot_list'),
]
