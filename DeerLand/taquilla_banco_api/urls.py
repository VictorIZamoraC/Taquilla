from django.urls import path

from taquilla_banco_api import views

urlpatterns = [
    path('solicitudTransferencia/', views.transferRequestView.as_view(), name='transferRequests_list'),
    path('solicitudTransferencia/<int:id>', views.transferRequestView.as_view(), name='transferRequests_process'),
    path('estadoTransferencia/', views.transferStatusView.as_view(), name='transferStates_list'),
    path('estadoTransferencia/<int:id>', views.transferStatusView.as_view(), name='transferStates_process'),
]