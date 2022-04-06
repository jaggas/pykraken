from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.get_open_orders_request_body import GetOpenOrdersRequestBody
from ...models.inline_response_20012 import InlineResponse20012
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    form_data: GetOpenOrdersRequestBody,
) -> Dict[str, Any]:
    url = "{}/private/OpenOrders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[InlineResponse20012]:
    if response.status_code == 200:
        response_200 = InlineResponse20012.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[InlineResponse20012]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: GetOpenOrdersRequestBody,
) -> Response[InlineResponse20012]:
    """Get Open Orders

     Retrieve information about currently open orders.

    Returns:
        Response[InlineResponse20012]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    form_data: GetOpenOrdersRequestBody,
) -> Optional[InlineResponse20012]:
    """Get Open Orders

     Retrieve information about currently open orders.

    Returns:
        Response[InlineResponse20012]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    form_data: GetOpenOrdersRequestBody,
) -> Response[InlineResponse20012]:
    """Get Open Orders

     Retrieve information about currently open orders.

    Returns:
        Response[InlineResponse20012]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    form_data: GetOpenOrdersRequestBody,
) -> Optional[InlineResponse20012]:
    """Get Open Orders

     Retrieve information about currently open orders.

    Returns:
        Response[InlineResponse20012]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
