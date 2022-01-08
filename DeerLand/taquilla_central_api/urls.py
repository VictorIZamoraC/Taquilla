from django.urls import path

from taquilla_central_api import views

urlpatterns = [
    path('pasesTaquilla/', views.passesBoxOfficeView.as_view(), name='passesBoxOffice_list'),
    path('pasesTaquilla/<int:id>', views.passesBoxOfficeView.as_view(), name='passesBoxOffice_process'),
    path('pasesVendidos/', views.passesSoldView.as_view(), name='passesSold_list'),
    path('pasesVendidos/<int:id>', views.passesSoldView.as_view(), name='passesSold_process'),
]