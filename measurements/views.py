from django.shortcuts import render
from .logic import variables_logic as vl
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurements = vl.get_measurements()
            measurements_dto = serializers.serialize('json', measurements)
            return HttpResponse(measurements_dto, 'application/json')
        else:
            measurements_dto = vl.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')
    if request.method == 'POST':
        measurement_dto = vl.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement = vl.get_measurement(pk)
        measurement_dto = serializers.serialize('json', measurement)
        return HttpResponse(measurement_dto, 'application/json')
    if request.method == 'PUT':
        measurement_dto = vl.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
