from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.inline_response_20028 import InlineResponse20028
from ...models.private_cancel_all_orders_after_body import PrivateCancelAllOrdersAfterBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    form_data: PrivateCancelAllOrdersAfterBody,
) -> Dict[str, Any]:
    url = "{}/private/CancelAllOrdersAfter".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[InlineResponse20028]:
    if response.status_code == 200:
        response_200 = InlineResponse20028.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[InlineResponse20028]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: PrivateCancelAllOrdersAfterBody,
) -> Response[InlineResponse20028]:
    """Cancel All Orders After X

     CancelAllOrdersAfter provides a \"Dead Man's Switch\" mechanism to protect the client from network
    malfunction, extreme latency or unexpected matching engine downtime. The client can send a request
    with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders
    when the timer expires. The client has to keep sending new requests to push back the trigger time,
    or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are
    cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

    The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.
    This allows the client to keep the orders in place in case of a brief disconnection or transient
    delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the
    timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders
    will be cancelled when the trading engine comes back from downtime - planned or otherwise).

    Returns:
        Response[InlineResponse20028]
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
    form_data: PrivateCancelAllOrdersAfterBody,
) -> Optional[InlineResponse20028]:
    """Cancel All Orders After X

     CancelAllOrdersAfter provides a \"Dead Man's Switch\" mechanism to protect the client from network
    malfunction, extreme latency or unexpected matching engine downtime. The client can send a request
    with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders
    when the timer expires. The client has to keep sending new requests to push back the trigger time,
    or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are
    cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

    The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.
    This allows the client to keep the orders in place in case of a brief disconnection or transient
    delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the
    timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders
    will be cancelled when the trading engine comes back from downtime - planned or otherwise).

    Returns:
        Response[InlineResponse20028]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    form_data: PrivateCancelAllOrdersAfterBody,
) -> Response[InlineResponse20028]:
    """Cancel All Orders After X

     CancelAllOrdersAfter provides a \"Dead Man's Switch\" mechanism to protect the client from network
    malfunction, extreme latency or unexpected matching engine downtime. The client can send a request
    with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders
    when the timer expires. The client has to keep sending new requests to push back the trigger time,
    or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are
    cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

    The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.
    This allows the client to keep the orders in place in case of a brief disconnection or transient
    delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the
    timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders
    will be cancelled when the trading engine comes back from downtime - planned or otherwise).

    Returns:
        Response[InlineResponse20028]
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
    form_data: PrivateCancelAllOrdersAfterBody,
) -> Optional[InlineResponse20028]:
    """Cancel All Orders After X

     CancelAllOrdersAfter provides a \"Dead Man's Switch\" mechanism to protect the client from network
    malfunction, extreme latency or unexpected matching engine downtime. The client can send a request
    with a timeout (in seconds), that will start a countdown timer which will cancel *all* client orders
    when the timer expires. The client has to keep sending new requests to push back the trigger time,
    or deactivate the mechanism by specifying a timeout of 0. If the timer expires, all orders are
    cancelled and then the timer remains disabled until the client provides a new (non-zero) timeout.

    The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds.
    This allows the client to keep the orders in place in case of a brief disconnection or transient
    delay, while keeping them safe in case of a network breakdown. It is also recommended to disable the
    timer ahead of regularly scheduled trading engine maintenance (if the timer is enabled, all orders
    will be cancelled when the trading engine comes back from downtime - planned or otherwise).

    Returns:
        Response[InlineResponse20028]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
