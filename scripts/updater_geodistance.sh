#!/bin/bash

[[ $(uname) == "Darwin" ]] && LAST_MONTH=$(date -v -1m "+%Y-%m") || LAST_MONTH=$(date --date="-1 month" +%Y-%m)
export LAST_MONTH
export MONTH=${MONTH:-$(date +%Y-%m)}
export FINDCEP_S3_STORAGE=${FINDCEP_S3_STORAGE:-"s3://findcep-data"}

echo ":: INIT FINDCEP GEOLOCATION CEP UPDATER ::"

python3 -m venv .venv && source .venv/bin/activate && python3 -m pip install -r requirements-dev.txt

aws s3 cp ${FINDCEP_S3_STORAGE}/npz/GEOCEP-${LAST_MONTH}.npz GEOCEP.npz
[ $? -ne 0 ] && exit 1

aws s3 cp ${FINDCEP_S3_STORAGE}/geo/geolocation-${MONTH}.json.gz .
[ $? -ne 0 ] && exit 1

echo ":: UPDATE FINDCEP API GEOLOCATION CEP ::"
python3 scripts/generate_geocep_npz.py geolocation-${MONTH}.json.gz
[ $? -ne 0 ] && exit 1

echo ":: FINDCEP GEOLOCATION CEP FINISH ::"
[ ! -s GEOCEP.npz ] && echo 1
aws s3 cp GEOCEP.npz s3://findcep-data/npz/GEOCEP-$MONTH.npz
[ $? -ne 0 ] && exit 1

mv GEOCEP.npz vendor/GEOCEP.npz
[ $? -ne 0 ] && exit 1

AWS_DEFAULT_REGION=sa-east-1 chalice deploy --stage prod
[ $? -ne 0 ] && exit 1

