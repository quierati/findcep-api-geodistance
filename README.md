# API GEO DISTANCE

Esta api tem a funcionalidade de calcular a distância entre dois pontos (cep ou latitude e longitude) com retorno em kilometros e metros, e suporta simulação aproximada para distância em rota.


### How to Deploy Production
Get the latest version of the geocep database
```sh
aws s3 cp s3://findcep-data/npz/GEOCEP-$(date +%Y-%m).npz vendor/GEOCEP.npz
```

Load python requirements
```sh
# load python env
. .venv/bin/activate || { python3 -m venv .venv; source .venv/bin/activate; }
pip install -U -r requirements.txt
````

Deploy app in brazil region
```sh
AWS_DEFAULT_REGION=sa-east-1 chalice deploy --stage prod
```

Create production dns registry
```sh
aws route53 change-resource-record-sets --hosted-zone-id Z1IO84G478HOTK --change-batch file://.chalice/route53.json
```

## Endpoint

Production
> https://geolocation-distance.api.findcep.com

Stage
> https://yy8eucz829.execute-api.sa-east-1.amazonaws.com/qa/

Dev
>

Local
> http://localhost:8000 

## Features

### cep to cep

> /v1/geolocation/distance/from/cep/{cep}/to/cep/{cep}
> /v1/geolocation/distance/from/cep/{cep}/to/cep/{cep}/approximate/{approx}

### cep to latlon

> /v1/geolocation/distance/from/cep/{cep}/to/latlon/{latlon}
> /v1/geolocation/distance/from/cep/{cep}/to/latlon/{latlon}/approximate/{approx}

### latlon to latlon

> /v1/geolocation/distance/from/latlon/{latlon}/to/latlon/{latlon}
> /v1/geolocation/distance/from/latlon/{latlon}/to/latlon/{latlon}/approximate/{approx}

