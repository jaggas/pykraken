#!/bin/bash

function create_kraken_api()
{
    local swagger_file="kraken-rest-api.yaml"

    echo "Creating Kraken API Python client"
    local swagger_filepath="$KRAKEN_API_HOME/conf/$swagger_file"
    openapi-python-client generate --path $swagger_filepath
    
    echo "Installing client API"
    rsync -av $KRAKEN_API_HOME/rest-api-client/rest_api_client $KRAKEN_API_HOME/pykraken --delete
    rm -Rf $KRAKEN_API_HOME/rest-api-client
}

export KRAKEN_API_HOME=$(pwd)
