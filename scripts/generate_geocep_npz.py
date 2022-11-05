#!/usr/bin/env python
import gzip
import json
from math import radians

from numpy import load as np_load 
from numpy import savez_compressed as np_savez_compressed


try:
    GEOCEP = np_load('GEOCEP.npz', allow_pickle=True)['cep'].item()
except Exception as e:
    GEOCEP = {}
    #raise Exception('ERROR: LOAD GEOCEP DATA FILE')


def parse(data):
    return data['postal_code'],(radians(data['location'].get('lat')),radians(data['location'].get('lng'))) 


def process(input_file):
    with gzip.open(input_file, 'rt') as f:
        for line in f:
            data = json.loads(line)
            try:
                yield parse(data)
            except:
                data['location'] = {'lat': 0, 'lng': 0}
                yield parse(data)


def execute(input_file):
    for cep,data in process(input_file):
        GEOCEP[cep] = data
    np_savez_compressed('GEOCEP.npz', cep=GEOCEP, allow_pickle=True)
        

if __name__ == '__main__':
    import sys
    execute(sys.argv[1])
 
