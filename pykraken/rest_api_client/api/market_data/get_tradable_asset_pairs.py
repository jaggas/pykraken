from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_tradable_asset_pairs_info import GetTradableAssetPairsInfo
from ...models.inline_response_2003 import InlineResponse2003
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    info: Union[Unset, None, GetTradableAssetPairsInfo] = GetTradableAssetPairsInfo.INFO,
) -> Dict[str, Any]:
    url = "{}/public/AssetPairs".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pair"] = pair

    json_info: Union[Unset, None, str] = UNSET
    if not isinstance(info, Unset):
        json_info = info.value if info else None

    params["info"] = json_info

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[InlineResponse2003]:
    if response.status_code == 200:
        response_200 = InlineResponse2003.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[InlineResponse2003]:
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
    info: Union[Unset, None, GetTradableAssetPairsInfo] = GetTradableAssetPairsInfo.INFO,
) -> Response[InlineResponse2003]:
    """Get Tradable Asset Pairs

     Get tradable asset pairs

    Args:
        pair (Union[Unset, None, str]):
        info (Union[Unset, None, GetTradableAssetPairsInfo]):  Default:
            GetTradableAssetPairsInfo.INFO.

    Returns:
        Response[InlineResponse2003]
    """

    kwargs = _get_kwargs(
        client=client,
        pair=pair,
        info=info,
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
    info: Union[Unset, None, GetTradableAssetPairsInfo] = GetTradableAssetPairsInfo.INFO,
) -> Optional[InlineResponse2003]:
    """Get Tradable Asset Pairs

     Get tradable asset pairs

    Args:
        pair (Union[Unset, None, str]):
        info (Union[Unset, None, GetTradableAssetPairsInfo]):  Default:
            GetTradableAssetPairsInfo.INFO.

    Returns:
        Response[InlineResponse2003]
    """

    return sync_detailed(
        client=client,
        pair=pair,
        info=info,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    info: Union[Unset, None, GetTradableAssetPairsInfo] = GetTradableAssetPairsInfo.INFO,
) -> Response[InlineResponse2003]:
    """Get Tradable Asset Pairs

     Get tradable asset pairs

    Args:
        pair (Union[Unset, None, str]):
        info (Union[Unset, None, GetTradableAssetPairsInfo]):  Default:
            GetTradableAssetPairsInfo.INFO.

    Returns:
        Response[InlineResponse2003]
    """

    kwargs = _get_kwargs(
        client=client,
        pair=pair,
        info=info,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    pair: Union[Unset, None, str] = UNSET,
    info: Union[Unset, None, GetTradableAssetPairsInfo] = GetTradableAssetPairsInfo.INFO,
) -> Optional[InlineResponse2003]:
    """Get Tradable Asset Pairs

     Get tradable asset pairs

    Args:
        pair (Union[Unset, None, str]):
        info (Union[Unset, None, GetTradableAssetPairsInfo]):  Default:
            GetTradableAssetPairsInfo.INFO.

    Returns:
        Response[InlineResponse2003]
    """

    return (
        await asyncio_detailed(
            client=client,
            pair=pair,
            info=info,
        )
    ).parsed
