# -*- encoding: utf-8 -*-
from math import radians

from numpy import load as np_load

from .harvesine import harvesine_geocep

GEOCEP = None
GEOCEP_FILE = 'GEOCEP.npz'
LATITUDE = -90.0000000
LONGITUDE = -180.0000000

try:
    GEOCEP = np_load('GEOCEP.npz', allow_pickle=True)['cep'].item()
except FileNotFoundError as e:
    GEOCEP = np_load('vendor/GEOCEP.npz', allow_pickle=True)['cep'].item()
except Exception as e:
    raise Exception('ERRO AO PROCESSAR O ARQUIVO GEOCEP: "{0}"'.format(e))


def validate_latlon(field):
    """ Latitude faixa de -90.0 a 90.0 e Longitude faixa de -180.0 a 180.0 """
    try:
        lat,lon = map(float, field.strip().split(','))
    except:
        raise Exception('LatLon "{0}" - Formato Inválido'.format(field))
    if lat < LATITUDE or lat > abs(LATITUDE):
        raise Exception('Latitude "{0}" - Faixa Inválida'.format(lat))
    if lon < LONGITUDE or lon > abs(LONGITUDE):
        raise Exception('Longitude "{0}" - Faixa Inválida'.format(lon))
    return (radians(lat),radians(lon))


def validate_cep(field):
    """ Faixa de cep 00000-000 a 99999-999 """
    cep = "".join(field.replace("-"," ").split())
    if not cep.isdigit() and len(cep) != 8:
        raise Exception('CEP "{0}" - Formato Inválido'.format(field))
    try:
        return GEOCEP[cep]
    except:
        raise Exception('CEP "{0}" - Não Existe'.format(field))


def validate_approx(field):
    """ Faixa 0 a 100 """
    try:
        approx = float(field)
    except:
        raise Exception('APPROXIMATE "{0}" - Formato Inválido'.format(field))
    if approx < 0.0 or approx > 100.0:
        raise Exception('APPROXIMATE "{0}" - Faixa Inválida'.format(field))
    return 1 + (approx / 100)


def distance_cep(cep, cep_to): 
    cep = validate_cep(cep)
    cep_to = validate_cep(cep_to)
    return harvesine_geocep(cep, cep_to)


def distance_cep_latlon(cep, latlon):
    cep = validate_cep(cep)
    latlon = validate_latlon(latlon)
    return harvesine_geocep(cep, latlon)


def distance_latlon(latlon, latlon_to): 
    latlon = validate_latlon(latlon)
    latlon_to = validate_latlon(latlon_to)
    return harvesine_geocep(latlon, latlon_to)

