#!/bin/bash

function create_kraken_api()
{
    echo "Creating Kraken API Python client"
    swagger_file="$KRAKEN_API_HOME/conf/kraken-restApi-swagger.yaml"
    openapi-python-client generate --path $swagger_file
    
    echo "Installing client API"
    rsync -av $KRAKEN_API_HOME/rest-api-client/rest_api_client $KRAKEN_API_HOME/pykraken --delete
    rm -Rf $KRAKEN_API_HOME/rest-api-client
}

export KRAKEN_API_HOME=$(pwd)
