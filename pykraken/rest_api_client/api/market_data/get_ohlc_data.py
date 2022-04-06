from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_ohlc_data_interval import GetOHLCDataInterval
from ...models.inline_response_2005 import InlineResponse2005
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, GetOHLCDataInterval] = GetOHLCDataInterval.VALUE_1,
    since: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/public/OHLC".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pair"] = pair

    json_interval: Union[Unset, None, int] = UNSET
    if not isinstance(interval, Unset):
        json_interval = interval.value if interval else None

    params["interval"] = json_interval

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


def _parse_response(*, response: httpx.Response) -> Optional[InlineResponse2005]:
    if response.status_code == 200:
        response_200 = InlineResponse2005.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[InlineResponse2005]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, GetOHLCDataInterval] = GetOHLCDataInterval.VALUE_1,
    since: Union[Unset, None, int] = UNSET,
) -> Response[InlineResponse2005]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        pair (Union[Unset, None, str]):
        interval (Union[Unset, None, GetOHLCDataInterval]):  Default: GetOHLCDataInterval.VALUE_1.
        since (Union[Unset, None, int]):

    Returns:
        Response[InlineResponse2005]
    """

    kwargs = _get_kwargs(
        client=client,
        pair=pair,
        interval=interval,
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
    pair: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, GetOHLCDataInterval] = GetOHLCDataInterval.VALUE_1,
    since: Union[Unset, None, int] = UNSET,
) -> Optional[InlineResponse2005]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        pair (Union[Unset, None, str]):
        interval (Union[Unset, None, GetOHLCDataInterval]):  Default: GetOHLCDataInterval.VALUE_1.
        since (Union[Unset, None, int]):

    Returns:
        Response[InlineResponse2005]
    """

    return sync_detailed(
        client=client,
        pair=pair,
        interval=interval,
        since=since,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, GetOHLCDataInterval] = GetOHLCDataInterval.VALUE_1,
    since: Union[Unset, None, int] = UNSET,
) -> Response[InlineResponse2005]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        pair (Union[Unset, None, str]):
        interval (Union[Unset, None, GetOHLCDataInterval]):  Default: GetOHLCDataInterval.VALUE_1.
        since (Union[Unset, None, int]):

    Returns:
        Response[InlineResponse2005]
    """

    kwargs = _get_kwargs(
        client=client,
        pair=pair,
        interval=interval,
        since=since,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    interval: Union[Unset, None, GetOHLCDataInterval] = GetOHLCDataInterval.VALUE_1,
    since: Union[Unset, None, int] = UNSET,
) -> Optional[InlineResponse2005]:
    """Get OHLC Data

     Note: the last entry in the OHLC array is for the current, not-yet-committed frame and will always
    be present, regardless of the value of `since`.

    Args:
        pair (Union[Unset, None, str]):
        interval (Union[Unset, None, GetOHLCDataInterval]):  Default: GetOHLCDataInterval.VALUE_1.
        since (Union[Unset, None, int]):

    Returns:
        Response[InlineResponse2005]
    """

    return (
        await asyncio_detailed(
            client=client,
            pair=pair,
            interval=interval,
            since=since,
        )
    ).parsed
