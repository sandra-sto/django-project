from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from predictions.models import  Predictions, Devices, PredictionModel, Data

from django.template import loader
def get_predictions_for_device(request):
    predictions = Predictions.objects.all().filter(device = request.GET.get("device_id"))

    list_dicts = [dict(i) for i in predictions]

    # template = loader.get_template('predictions/predictions.html')
    devices_types = Devices.objects.values_list("device_type", flat=True)
    devices_types_list = list(devices_types)

    context = {'predictions': list_dicts}
    context = {'device_types' : devices_types}
    return render(request, 'predictions/predictions.html', context)
    # return JsonResponse(list_dicts, safe=False)
    # return HttpResponse(json.dumps(listg), content_type = "application/json")


def get_devices(request):
    devices = Devices.objects.allow_filtering().filter(device_type = request.GET["device_type"]).values_list("device_id", flat=True)
    devices_list=list(devices)

    return JsonResponse(devices_list, safe=False)

def get_devices_types(request):
    devices_types = Devices.objects.values_list("device_type", flat=True)
    devices_types_list = list(devices_types)
    return JsonResponse(devices_types_list, safe=False)

def get_prediction_models_for_devices(request):
    models = PredictionModel.objects.filter(device=request.GET["device"])
    list_dicts = [dict(i) for i in models]
    return JsonResponse(list_dicts, safe=False)

def get_data_for_device_and_parameter(request):
    data = Data.objects.all().allow_filtering().filter(device_id=request.GET["device"],
                                     parameter_name=request.GET["parameter"])
    list_dicts = [dict(i) for i in data]
    return JsonResponse(list_dicts, safe=False)