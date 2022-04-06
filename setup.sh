#!/bin/bash

function create_kraken_api()
{
    rm -Rf $KRAKEN_API_HOME/rest-api-client
    echo "Creating Kraken API Python client"
    local swagger_raw="$KRAKEN_API_HOME/conf/kraken_openapi_spec.yaml"
    local swagger_resolved="$KRAKEN_API_HOME/conf/kraken_openapi_spec_resolved.yaml"

    # Create resolved swagger file
    echo "Creating resolved OpenAPI spec YAML"
    swagger-cli bundle -o $swagger_resolved -r -t yaml $swagger_raw

    # Generate client Python SDK
    openapi-python-client generate --path $swagger_resolved --fail-on-warning 2>&1 | tee "kraken_openapi_log.txt"
    
    echo "Installing client API"
    rsync -av $KRAKEN_API_HOME/rest-api-client/rest_api_client $KRAKEN_API_HOME/pykraken --delete
    rm -Rf $KRAKEN_API_HOME/rest-api-client
}

export KRAKEN_API_HOME=$(pwd)
