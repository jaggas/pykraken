from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.get_ledgers_info_request_body import GetLedgersInfoRequestBody
from ...models.inline_response_20018 import InlineResponse20018
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    form_data: GetLedgersInfoRequestBody,
) -> Dict[str, Any]:
    url = "{}/private/Ledgers".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[InlineResponse20018]:
    if response.status_code == 200:
        response_200 = InlineResponse20018.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[InlineResponse20018]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: GetLedgersInfoRequestBody,
) -> Response[InlineResponse20018]:
    """Get Ledgers Info

     Retrieve information about ledger entries. 50 results are returned at a time, the most recent by
    default.

    Returns:
        Response[InlineResponse20018]
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
    form_data: GetLedgersInfoRequestBody,
) -> Optional[InlineResponse20018]:
    """Get Ledgers Info

     Retrieve information about ledger entries. 50 results are returned at a time, the most recent by
    default.

    Returns:
        Response[InlineResponse20018]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    form_data: GetLedgersInfoRequestBody,
) -> Response[InlineResponse20018]:
    """Get Ledgers Info

     Retrieve information about ledger entries. 50 results are returned at a time, the most recent by
    default.

    Returns:
        Response[InlineResponse20018]
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
    form_data: GetLedgersInfoRequestBody,
) -> Optional[InlineResponse20018]:
    """Get Ledgers Info

     Retrieve information about ledger entries. 50 results are returned at a time, the most recent by
    default.

    Returns:
        Response[InlineResponse20018]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
