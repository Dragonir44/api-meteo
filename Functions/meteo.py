from Data.city import meteo

def get_meteo_by_day(id):
    for day in meteo['forecast']:
        if day['day'] == int(id):
            return day
    return None