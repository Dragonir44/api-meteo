from flask import render_template, jsonify, request
from Config import app, BASE_METEO_API_URL, METEO_API_TOKEN
from Data.city import meteo
from Functions.meteo import get_meteo_by_day
import json, requests

@app.route('/')
def index():
    return render_template('index.html', meteo = meteo)


@app.route('/day/<id>')
def getMeteoByDay(id):
    day = get_meteo_by_day(id)
    return render_template('day.html', day=day)

@app.route('/api/search', methods=['GET', 'POST'])
def getMeteoByCity():
    if request.method == 'GET':
        return render_template('apimeteo.html')
    if request.method == 'POST':
        cityName = request.form.get("city")
        searchResult = requests.get(f"{BASE_METEO_API_URL}/location/cities?token={METEO_API_TOKEN}&search={cityName}")
        data = json.loads(searchResult.content.decode('utf-8'))
        firstSearchDataCode = data['cities'][0]['insee']
        
        meteoResult = requests.get(f"{BASE_METEO_API_URL}/forecast/daily?token={METEO_API_TOKEN}&insee={firstSearchDataCode}")
        
        formatedResult = json.loads(meteoResult.content.decode('utf-8'))
        
        # for data in formatedResult['forecast']:
        #     print(data)
        
        return render_template('apimeteo.html', data=formatedResult)