from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from taquilla_banco_api.models import transferRequest, transferStatus


class transferRequestView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if (id>0):
            transfer_requests = list(transferRequest.objects.filter(id=id).values())
            if  len(transfer_requests) > 0:
                transfer_request = transfer_requests[0]
                datos = {'message': "Success", 'transfer_Request': transfer_request}
            else:
                datos = {'message': "Solicitud no encontrada ..."}
            return JsonResponse(datos)
        else:
            transfer_requests = list(transferRequest.objects.values())

            if  len(transfer_requests) > 0:
                datos = {'message': "Success", 'transfer_Requests': transfer_requests}
            else: 
                datos = {'message': "Solicitudes no encontradas ..."}
            return JsonResponse(datos)

    def post(self, request):
        
        jd = json.loads(request.body)
        transferRequest.objects.create(destinyAccount=jd['destinyAccount'], 
        originAccount=jd['originAccount'], cvv=jd['cvv'], expDate=jd['expDate'],
        ammount=jd['ammount'], concept=jd['concept'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        transfer_requests = list(transferRequest.objects.filter(id=id).values())
        
        if  len(transfer_requests) > 0:
            transfer_request = transferRequest.objects.get(id=id)
            transfer_request.destinyAccount=jd['destinyAccount']
            transfer_request.originAccount=jd['originAccount']
            transfer_request.cvv=jd['cvv']
            transfer_request.expDate=jd['expDate']
            transfer_request.ammount=jd['ammount']
            transfer_request.concept=jd['concept']
            transfer_request.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Solicitud no encontrada ..."}
        return JsonResponse(datos)

    def delete(self, request, id):

        transfer_requests = list(transferRequest.objects.filter(id=id).values())
        if  len(transfer_requests) > 0:
            transferRequest.objects.filter(id=id).delete()
            datos = {'message': "Success"} 
        else:
            datos = {'message': "Solicitud no encontrada ..."}
        return JsonResponse(datos)


class transferStatusView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if (id>0):
            transfer_states = list(transferStatus.objects.filter(id=id).values())
            if  len(transfer_states) > 0:
                transfer_status = transfer_states[0]
                datos = {'message': "Success", 'transfer_Status': transfer_status}
            else:
                datos = {'message': "Transacción no encontrada ..."}
            return JsonResponse(datos)
        else:
            transfer_states = list(transferStatus.objects.values())

            if  len(transfer_states) > 0:
                datos = {'message': "Success", 'transfer_States': transfer_states}
            else: 
                datos = {'message': "Transacciones no encontradas ..."}
            return JsonResponse(datos)

    def post(self, request):
        
        jd = json.loads(request.body)
        transferStatus.objects.create(transactionNum=jd['transactionNum'], 
        status=jd['status'], date=jd['date'], ammount=jd['ammount'],
        origin=jd['origin'], destiny=jd['destiny'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        transfer_states = list(transferStatus.objects.filter(id=id).values())
        
        if  len(transfer_states) > 0:
            transfer_status = transferStatus.objects.get(id=id)
            transfer_status.transactionNum=jd['transactionNum']
            transfer_status.status=jd['status']
            transfer_status.date=jd['date']
            transfer_status.ammount=jd['ammount']
            transfer_status.origin=jd['origin']
            transfer_status.destiny=jd['destiny']
            transfer_status.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Transacción no encontrada ..."}
        return JsonResponse(datos)

    def delete(self, request, id):

        transfer_states = list(transferStatus.objects.filter(id=id).values())
        if  len(transfer_states) > 0:
            transferStatus.objects.filter(id=id).delete()
            datos = {'message': "Success"} 
        else:
            datos = {'message': "Transacción no encontrada ..."}
        return JsonResponse(datos)