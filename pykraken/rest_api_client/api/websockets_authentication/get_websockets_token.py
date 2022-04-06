from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.get_websockets_token_response_200 import GetWebsocketsTokenResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/private/GetWebSocketsToken".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetWebsocketsTokenResponse200]:
    if response.status_code == 200:
        response_200 = GetWebsocketsTokenResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetWebsocketsTokenResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[GetWebsocketsTokenResponse200]:
    """Get Websockets Token

     An authentication token must be requested via this REST API endpoint in order to connect to and
    authenticate with our [Websockets API](https://docs.kraken.com). The token should be used within 15
    minutes of creation, but it does not expire once a successful Websockets connection and private
    subscription has been made and is maintained.

    > The 'Access WebSockets API' permission must be enabled for the API key in order to generate the
    authentication token.

    Returns:
        Response[GetWebsocketsTokenResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[GetWebsocketsTokenResponse200]:
    """Get Websockets Token

     An authentication token must be requested via this REST API endpoint in order to connect to and
    authenticate with our [Websockets API](https://docs.kraken.com). The token should be used within 15
    minutes of creation, but it does not expire once a successful Websockets connection and private
    subscription has been made and is maintained.

    > The 'Access WebSockets API' permission must be enabled for the API key in order to generate the
    authentication token.

    Returns:
        Response[GetWebsocketsTokenResponse200]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[GetWebsocketsTokenResponse200]:
    """Get Websockets Token

     An authentication token must be requested via this REST API endpoint in order to connect to and
    authenticate with our [Websockets API](https://docs.kraken.com). The token should be used within 15
    minutes of creation, but it does not expire once a successful Websockets connection and private
    subscription has been made and is maintained.

    > The 'Access WebSockets API' permission must be enabled for the API key in order to generate the
    authentication token.

    Returns:
        Response[GetWebsocketsTokenResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[GetWebsocketsTokenResponse200]:
    """Get Websockets Token

     An authentication token must be requested via this REST API endpoint in order to connect to and
    authenticate with our [Websockets API](https://docs.kraken.com). The token should be used within 15
    minutes of creation, but it does not expire once a successful Websockets connection and private
    subscription has been made and is maintained.

    > The 'Access WebSockets API' permission must be enabled for the API key in order to generate the
    authentication token.

    Returns:
        Response[GetWebsocketsTokenResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
