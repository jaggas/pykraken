from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.get_deposit_addresses_response_200 import GetDepositAddressesResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/private/DepositAddresses".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetDepositAddressesResponse200]:
    if response.status_code == 200:
        response_200 = GetDepositAddressesResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetDepositAddressesResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[GetDepositAddressesResponse200]:
    """Get Deposit Addresses

     Retrieve (or generate a new) deposit addresses for a particular asset and method.

    Returns:
        Response[GetDepositAddressesResponse200]
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
) -> Optional[GetDepositAddressesResponse200]:
    """Get Deposit Addresses

     Retrieve (or generate a new) deposit addresses for a particular asset and method.

    Returns:
        Response[GetDepositAddressesResponse200]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[GetDepositAddressesResponse200]:
    """Get Deposit Addresses

     Retrieve (or generate a new) deposit addresses for a particular asset and method.

    Returns:
        Response[GetDepositAddressesResponse200]
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
) -> Optional[GetDepositAddressesResponse200]:
    """Get Deposit Addresses

     Retrieve (or generate a new) deposit addresses for a particular asset and method.

    Returns:
        Response[GetDepositAddressesResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
