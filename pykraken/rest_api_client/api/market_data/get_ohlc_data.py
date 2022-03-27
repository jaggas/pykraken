from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_ohlc_data_response_200 import GetOHLCDataResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    since: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/public/OHLC".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["since"] = since

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetOHLCDataResponse200]:
    if response.status_code == 200:
        response_200 = GetOHLCDataResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetOHLCDataResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    since: Union[Unset, None, int] = UNSET,
) -> Response[GetOHLCDataResponse200]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        since (Union[Unset, None, int]):

    Returns:
        Response[GetOHLCDataResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        since=since,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    since: Union[Unset, None, int] = UNSET,
) -> Optional[GetOHLCDataResponse200]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        since (Union[Unset, None, int]):

    Returns:
        Response[GetOHLCDataResponse200]
    """

    return sync_detailed(
        client=client,
        since=since,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    since: Union[Unset, None, int] = UNSET,
) -> Response[GetOHLCDataResponse200]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        since (Union[Unset, None, int]):

    Returns:
        Response[GetOHLCDataResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        since=since,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    since: Union[Unset, None, int] = UNSET,
) -> Optional[GetOHLCDataResponse200]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        since (Union[Unset, None, int]):

    Returns:
        Response[GetOHLCDataResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            since=since,
        )
    ).parsed
