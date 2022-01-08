from django.urls import path

from taquilla_experiencia_api import views

urlpatterns = [
    path('registrarCliente/', views.registerCustomerView.as_view(), name='registerCustomer_list'),
    path('registrarCliente/<int:id>', views.registerCustomerView.as_view(), name='registerCustomer_process'),
    path('promocionTaquilla/', views.promotionsBoxOfficeView.as_view(), name='promotionsBoxOffice_list'),
    path('promocionTaquilla/<int:id>', views.promotionsBoxOfficeView.as_view(), name='promotionsBoxOffice_process'),
]