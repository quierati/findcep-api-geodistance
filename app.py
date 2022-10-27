from chalice import Chalice
from chalice import ChaliceViewError, BadRequestError, Response

from chalice.app import logging

from chalicelib.utils import (
    distance_cep, 
    distance_cep_latlon, 
    distance_latlon, 
    validate_approx
)

app = Chalice(app_name='findcep-api-geolocation-distance')
app.api.cors = True
app.log.setLevel(logging.INFO)


@app.route('/')
@app.route('/v1')
@app.route('/distance')
@app.route('/geolocation/distance')
def index():
    app.log.info("index")
    return {'api': 'findcep', 'method': 'geolocation_distance', 'version': 1}


@app.route('/geolocation/distance/from/cep/{cep}/to/cep/{cep_to}')
@app.route('/v1/geolocation/distance/from/cep/{cep}/to/cep/{cep_to}')
def _index_cep_to_cep(cep, cep_to):
    try:
        distance = distance_cep(cep, cep_to)
    except:
        return Response(body={'status': 'cep_invalid', 'code': 'error', 'status_code': 404}, status_code=404)
    return {"distance": distance, "formula": "haversine", "unit": "km", "distance_in_meters": round(distance*1000)} 
    

@app.route('/geolocation/distance/from/cep/{cep}/to/cep/{cep_to}/approximate/{approx}')
@app.route('/v1/geolocation/distance/from/cep/{cep}/to/cep/{cep_to}/approximate/{approx}')
def _index_cep_to_cep_approx(cep, cep_to, approx=15):
    try:
        distance = distance_cep(cep, cep_to)
    except:
        return Response(body={'status': 'cep_invalid', 'code': 'error', 'status_code': 404}, status_code=404)
    try:
        approx = validate_approx(approx)
    except:
        return Response(body={'status': 'approximate_invalid', 'code': 'error', 'status_code': 400}, status_code=400)
    return {"distance": distance, "approximate_distance_to_route": distance*approx, "formula": "haversine", "unit": "km", "distance_in_meters": round(distance*1000)} 
    


@app.route('/geolocation/distance/from/cep/{cep}/to/latlon/{latlon}')
@app.route('/v1/geolocation/distance/from/cep/{cep}/to/latlon/{latlon}')
def _index_cep_to_latlon(cep, latlon):
    try:
        distance = distance_cep_latlon(cep, latlon)
    except:
        return Response(body={'status': 'latlon_invalid', 'code': 'error', 'status_code': 404}, status_code=404)
    return {"distance": distance, "formula": "haversine", "unit": "km", "distance_in_meters": round(distance*1000)} 


@app.route('/geolocation/distance/from/cep/{cep}/to/latlon/{latlon}/approximate/{approx}')
@app.route('/v1/geolocation/distance/from/cep/{cep}/to/latlon/{latlon}/approximate/{approx}')
def _index_cep_to_latlon_approx(cep, latlon, approx=15):
    try:
        distance = distance_cep_latlon(cep, latlon)
    except:
        return Response(body={'status': 'cep_invalid', 'code': 'error', 'status_code': 404}, status_code=404)
    try:
        approx = validate_approx(approx)
    except:
        return Response(body={'status': 'approximate_invalid', 'code': 'error', 'status_code': 400}, status_code=400)
    return {"distance": distance, "approximate_distance_to_route": distance*approx, "formula": "haversine", "unit": "km", "distance_in_meters": round(distance*1000)} 
    

@app.route('/geolocation/distance/from/latlon/{latlon}/to/latlon/{latlon_to}')
@app.route('/v1/geolocation/distance/from/latlon/{latlon}/to/latlon/{latlon_to}')
def _index_latlon_to_latlon(latlon, latlon_to):
    try:
        distance = distance_latlon(latlon, latlon_to)
    except:
        return Response(body={'status': 'latlon_invalid', 'code': 'error', 'status_code': 404}, status_code=404)
    return {"distance": distance, "formula": "haversine", "unit": "km", "distance_in_meters": round(distance*1000)} 


@app.route('/geolocation/distance/from/latlon/{latlon}/to/latlon/{latlon_to}/approximate/{approx}')
@app.route('/v1/geolocation/distance/from/latlon/{latlon}/to/latlon/{latlon_to}/approximate/{approx}')
def _index_latlon_to_latlon_approx(latlon, latlon_to, approx=15):
    try:
        distance = distance_latlon(latlon, latlon_to)
    except:
        return Response(body={'status': 'cep_invalid', 'code': 'error', 'status_code': 404}, status_code=404)
    try:
        approx = validate_approx(approx)
    except:
        return Response(body={'status': 'approximate_invalid', 'code': 'error', 'status_code': 400}, status_code=400)
    return {"distance": distance, "approximate_distance_to_route": distance*approx, "formula": "haversine", "unit": "km", "distance_in_meters": round(distance*1000)} 
    
