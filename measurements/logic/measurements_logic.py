from .. models import Measurement


def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_pk):
    measurement = measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_var):
    measurement = get_measurement(mea_pk)
    measurement.variable = new_var["variable"]
    measurement.value = new_var["value"]
    measurement.unit = new_var["unit"]
    measurement.place = new_var["place"]
    measurement.dateTime = new_var["dateTime"]
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = measurement(  variable = var["variable"],
                                value = var["value"],
                                unit = var["unit"],
                                place = var["place"],
                                dateTime = var["dateTime"]
                                )

    measurement.save()
    return measurement

