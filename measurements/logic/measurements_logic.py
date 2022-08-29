from tkinter import Variable
from .. models import Measurement
from datetime import datetime
from variables.models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_var):
    date = datetime.strptime(new_var["dateTime"], "%d/%m/%Y %H:%M:%S")
    measurement = get_measurement(mea_pk)
    measurement.variable=Variable.objects.get(pk=new_var["variable"])
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.dateTime = date
    measurement.save()
    return measurement

def create_measurement(var):
    date = datetime.strptime(var["dateTime"], "%d/%m/%Y %H:%M:%S")
    measurement = Measurement( variable=Variable.objects.get(pk=var["variable"]),
                                value = var["value"],
                                unit = var["unit"],
                                place = var["place"],
                                dateTime = date,
                                )
    measurement.save()
    return measurement

def delete_measurement(var_pk):
    measurement=get_measurement(var_pk)
    measurement.delete()
