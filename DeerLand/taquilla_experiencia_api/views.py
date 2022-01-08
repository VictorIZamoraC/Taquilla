from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from taquilla_experiencia_api.models import promotionsBoxOffice, registerCustomer

# Create your views here.

class registerCustomerView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        
        if (id>0):
            register_customers = list(registerCustomer.objects.filter(id=id).values())
            if  len(register_customers) > 0:
                register_customer = register_customers[0]
                datos = {'message': "Success", 'register_Customer': register_customer}
            else:
                datos = {'message': "Registro no encontrado ..."}
            return JsonResponse(datos)
        else:
            register_customers = list(registerCustomer.objects.values())

            if  len(register_customers) > 0:
                datos = {'message': "Success", 'register_Customers': register_customers}
            else: 
                datos = {'message': "Registros no encontrados ..."}
            return JsonResponse(datos)

    def post(self, request):
        
        jd = json.loads(request.body)
        registerCustomer.objects.create(clientCode=jd['clientCode'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
      
        jd = json.loads(request.body)
        register_customers = list(registerCustomer.objects.filter(id=id).values())
        
        if  len(register_customers) > 0:
            register_customer = registerCustomer.objects.get(id=id)
            register_customer.clientCode=jd['clientCode']
            register_customer.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Registro no encontrado ..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        
        register_customers = list(registerCustomer.objects.filter(id=id).values())
        if  len(register_customers) > 0:
            registerCustomer.objects.filter(id=id).delete()
            datos = {'message': "Success"} 
        else:
            datos = {'message': "Registro no encontrado ..."}
        return JsonResponse(datos)


class promotionsBoxOfficeView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
       
        if (id>0):
            promotions_BoxOffice = list(promotionsBoxOffice.objects.filter(id=id).values())
            if  len(promotions_BoxOffice) > 0:
                promotion_BoxOffice = promotions_BoxOffice[0]
                datos = {'message': "Success", 'promotion_BoxOffice': promotion_BoxOffice}
            else:
                datos = {'message': "Promoción no encontrada ..."}
            return JsonResponse(datos)
        else:
            promotions_BoxOffice = list(promotionsBoxOffice.objects.values())

            if  len(promotions_BoxOffice) > 0:
                datos = {'message': "Success", 'promotions_BoxOffice': promotions_BoxOffice}
            else: 
                datos = {'message': "Promociones no encontradas ..."}
            return JsonResponse(datos)

    def post(self, request):
        
        jd = json.loads(request.body)
        promotionsBoxOffice.objects.create(idPass=jd['idPass'], discount=jd['discount'],
        expDate=jd['expDate'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        
        jd = json.loads(request.body)
        promotions_BoxOffice = list(promotionsBoxOffice.objects.filter(id=id).values())
        
        if  len(promotions_BoxOffice) > 0:
            promotion_BoxOffice = promotionsBoxOffice.objects.get(id=id)
            promotion_BoxOffice.idPass=jd['idPass']
            promotion_BoxOffice.discount=jd['discount']
            promotion_BoxOffice.expDate=jd['expDate']
            promotion_BoxOffice.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Promoción no encontrada ..."}
        return JsonResponse(datos)


    def delete(self, request, id):
        
        promotions_BoxOffice = list(promotionsBoxOffice.objects.filter(id=id).values())
        if  len(promotions_BoxOffice) > 0:
            promotionsBoxOffice.objects.filter(id=id).delete()
            datos = {'message': "Success"} 
        else:
            datos = {'message': "Promoción no encontrada ..."}
        return JsonResponse(datos)