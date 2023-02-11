from django.shortcuts import render
from .logic import variables_logic as vl
from django.http import HttpResponse
from django.core import serializers

def measurements_view(request):
    if request.method == 'GET':
        measurements = vl.get_measurements()
        measurements_dto = serializers.serialize('json', measurements)
        return HttpResponse(measurements_dto, 'application/json')

def measurement_view(request, pk):
    if request.method == 'GET':
        measurement = vl.get_measurement(pk)
        measurement_dto = serializers.serialize('json', measurement)
        return HttpResponse(measurement_dto, 'application/json')