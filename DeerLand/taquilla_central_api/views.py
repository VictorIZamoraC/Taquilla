from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from taquilla_central_api.models import passesBoxOffice, passesSold

# Create your views here.

class passesBoxOfficeView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        
        if (id>0):
            passes_boxoffice = list(passesBoxOffice.objects.filter(id=id).values())
            if  len(passes_boxoffice) > 0:
                pass_boxoffice = passes_boxoffice[0]
                datos = {'message': "Success", 'pass_BoxOffice': pass_boxoffice}
            else:
                datos = {'message': "Pase no encontrado ..."}
            return JsonResponse(datos)
        else:
            passes_boxoffice = list(passesBoxOffice.objects.values())

            if  len(passes_boxoffice) > 0:
                datos = {'message': "Success", 'passes_BoxOffice': passes_boxoffice}
            else: 
                datos = {'message': "Pases no encontrados ..."}
            return JsonResponse(datos)

    def post(self, request):
        
        jd = json.loads(request.body)
        passesBoxOffice.objects.create(passName=jd['passName'], passDescription=jd['passDescription'],
        passPrice=jd['passPrice'], passAvailability=jd['passAvailability'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
      
        jd = json.loads(request.body)
        passes_boxoffice = list(passesBoxOffice.objects.filter(id=id).values())
        
        if  len(passes_boxoffice) > 0:
            pass_boxoffice = passesBoxOffice.objects.get(id=id)
            pass_boxoffice.passName=jd['passName']
            pass_boxoffice.passDescription=jd['passDescription']
            pass_boxoffice.passPrice=jd['passPrice']
            pass_boxoffice.passAvailability=jd['passAvailability']
            pass_boxoffice.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Pase no encontrado ..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        
        passes_boxoffice = list(passesBoxOffice.objects.filter(id=id).values())
        if  len(passes_boxoffice) > 0:
            passesBoxOffice.objects.filter(id=id).delete()
            datos = {'message': "Success"} 
        else:
            datos = {'message': "Pase no encontrado ..."}
        return JsonResponse(datos)

class passesSoldView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        
        if (id>0):
            passes_sold = list(passesSold.objects.filter(id=id).values())
            if  len(passes_sold) > 0:
                pass_sold = passes_sold[0]
                datos = {'message': "Success", 'pass_Sold': pass_sold}
            else:
                datos = {'message': "Pase no encontrado ..."}
            return JsonResponse(datos)
        else:
            passes_sold = list(passesSold.objects.values())

            if  len(passes_sold) > 0:
                datos = {'message': "Success", 'passes_Sold': passes_sold}
            else: 
                datos = {'message': "Pases no encontrados ..."}
            return JsonResponse(datos)

    def post(self, request):
        
        jd = json.loads(request.body)
        passesSold.objects.create(idTransaction=jd['idTransaction'], account=jd['account'],
        date=jd['date'],customerName=jd['customerName'], passName=jd['passName'], 
        ammount=jd['ammount'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
      
        jd = json.loads(request.body)
        passes_sold = list(passesSold.objects.filter(id=id).values())
        
        if  len(passes_sold) > 0:
            pass_sold = passesSold.objects.get(id=id)
            pass_sold.idTransaction=jd['idTransaction']
            pass_sold.account=jd['account']
            pass_sold.date=jd['date']
            pass_sold.customerName=jd['customerName']
            pass_sold.passName=jd['passName']
            pass_sold.ammount=jd['ammount']
            pass_sold.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Pase no encontrado ..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        
        passes_sold = list(passesSold.objects.filter(id=id).values())
        if  len(passes_sold) > 0:
            passesSold.objects.filter(id=id).delete()
            datos = {'message': "Success"} 
        else:
            datos = {'message': "Pase no encontrado ..."}
        return JsonResponse(datos)