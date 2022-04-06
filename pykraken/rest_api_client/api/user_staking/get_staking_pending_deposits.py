from typing import Any, Dict

import httpx

from ...client import Client
from ...models.staking_pending_body import StakingPendingBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    form_data: StakingPendingBody,
) -> Dict[str, Any]:
    url = "{}/private/Staking/Pending".format(client.base_url)

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
    form_data: StakingPendingBody,
) -> Response[Any]:
    """Get Pending Staking Transactions

     Returns the list of pending staking transactions. Once resolved, these transactions
    will appear on the `List of Staking Transactions` endpoint.

    This operation requires an API key with both `Query funds` and `Withdraw funds` permissions.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    *,
    client: Client,
    form_data: StakingPendingBody,
) -> Response[Any]:
    """Get Pending Staking Transactions

     Returns the list of pending staking transactions. Once resolved, these transactions
    will appear on the `List of Staking Transactions` endpoint.

    This operation requires an API key with both `Query funds` and `Withdraw funds` permissions.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
