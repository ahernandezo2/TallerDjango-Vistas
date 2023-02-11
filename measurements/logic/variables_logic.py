from ..models import Measurement
from variables.logic import variables_logic as vl

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    fk=new_var["variable"]
    if vl.get_variable(fk)!=None:
        measurement.variable= vl.get_variable(fk)
        measurement.value= new_var["value"]
        measurement.place= new_var["place"]
        measurement.unit = new_var["unit"]
        measurement.save()
    return measurement

def create_measurement(var):
    fk=var["variable"]
    if vl.get_variable(fk)!=None:
        measurement = Measurement(variable = vl.get_variable(fk),value=var["value"],place=var["place"],unit=var["unit"])
        measurement.save()
    return measurement

def delete_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    measurement.delete()
    return measurement