from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.inline_response_2007 import InlineResponse2007
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    since: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/public/Trades".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pair"] = pair

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


def _parse_response(*, response: httpx.Response) -> Optional[InlineResponse2007]:
    if response.status_code == 200:
        response_200 = InlineResponse2007.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[InlineResponse2007]:
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
    since: Union[Unset, None, str] = UNSET,
) -> Response[InlineResponse2007]:
    """Get Recent Trades

     Returns the last 1000 trades by default

    Args:
        pair (Union[Unset, None, str]):
        since (Union[Unset, None, str]):

    Returns:
        Response[InlineResponse2007]
    """

    kwargs = _get_kwargs(
        client=client,
        pair=pair,
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
    since: Union[Unset, None, str] = UNSET,
) -> Optional[InlineResponse2007]:
    """Get Recent Trades

     Returns the last 1000 trades by default

    Args:
        pair (Union[Unset, None, str]):
        since (Union[Unset, None, str]):

    Returns:
        Response[InlineResponse2007]
    """

    return sync_detailed(
        client=client,
        pair=pair,
        since=since,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    since: Union[Unset, None, str] = UNSET,
) -> Response[InlineResponse2007]:
    """Get Recent Trades

     Returns the last 1000 trades by default

    Args:
        pair (Union[Unset, None, str]):
        since (Union[Unset, None, str]):

    Returns:
        Response[InlineResponse2007]
    """

    kwargs = _get_kwargs(
        client=client,
        pair=pair,
        since=since,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    since: Union[Unset, None, str] = UNSET,
) -> Optional[InlineResponse2007]:
    """Get Recent Trades

     Returns the last 1000 trades by default

    Args:
        pair (Union[Unset, None, str]):
        since (Union[Unset, None, str]):

    Returns:
        Response[InlineResponse2007]
    """

    return (
        await asyncio_detailed(
            client=client,
            pair=pair,
            since=since,
        )
    ).parsed
