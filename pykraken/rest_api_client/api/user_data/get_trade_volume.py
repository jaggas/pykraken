from typing import Any, Dict, Union

import httpx

from ...client import Client
from ...models.get_trade_volume import GetTradeVolume
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    form_data: GetTradeVolume,
    pair: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/private/TradeVolume".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pair"] = pair

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": form_data.to_dict(),
        "params": params,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    form_data: GetTradeVolume,
    pair: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get Trade Volume

     Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in `fees` and maker
    side in `fees_maker`. For pairs not on maker/taker, they will only be given in `fees`.

    Args:
        pair (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        pair=pair,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    form_data: GetTradeVolume,
    pair: Union[Unset, None, str] = UNSET,
) -> Response[Any]:
    """Get Trade Volume

     Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in `fees` and maker
    side in `fees_maker`. For pairs not on maker/taker, they will only be given in `fees`.

    Args:
        pair (Union[Unset, None, str]):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
        pair=pair,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
