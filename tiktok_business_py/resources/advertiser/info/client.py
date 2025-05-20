import typing
import typing_extensions

from tiktok_business_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
    type_utils,
)
from tiktok_business_py.types import models


class InfoClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        advertiser_ids: typing.List[str],
        fields: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal[
                        "balance", "currency", "name", "status", "timezone"
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.StandardResponse:
        """
        Get ad account details

        Retrieve detailed information about one or more advertising accounts.

        For more details, see [Advertiser Info](https://business-api.tiktok.com/portal/docs?id=1739593083610113).


        GET /advertiser/info

        Args:
            fields: A list of fields to include in the response. If not specified, all available fields will be returned.

        Available fields include:
        - name: Account name
        - status: Account status
        - currency: Account currency
        - timezone: Account timezone
        - balance: Account balance

            advertiser_ids: A list of advertiser account IDs to retrieve information for.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successfully retrieved advertiser information

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.advertiser.info.list(advertiser_ids=["T69303382030970061B"])
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "advertiser_ids",
            to_encodable(item=advertiser_ids, dump_with=typing.List[str]),
            style="form",
            explode=False,
        )
        if not isinstance(fields, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fields",
                to_encodable(
                    item=fields,
                    dump_with=typing.List[
                        typing_extensions.Literal[
                            "balance", "currency", "name", "status", "timezone"
                        ]
                    ],
                ),
                style="form",
                explode=False,
            )
        return self._base_client.request(
            method="GET",
            path="/advertiser/info",
            auth_names=["token"],
            query_params=_query,
            cast_to=models.StandardResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncInfoClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        advertiser_ids: typing.List[str],
        fields: typing.Union[
            typing.Optional[
                typing.List[
                    typing_extensions.Literal[
                        "balance", "currency", "name", "status", "timezone"
                    ]
                ]
            ],
            type_utils.NotGiven,
        ] = type_utils.NOT_GIVEN,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.StandardResponse:
        """
        Get ad account details

        Retrieve detailed information about one or more advertising accounts.

        For more details, see [Advertiser Info](https://business-api.tiktok.com/portal/docs?id=1739593083610113).


        GET /advertiser/info

        Args:
            fields: A list of fields to include in the response. If not specified, all available fields will be returned.

        Available fields include:
        - name: Account name
        - status: Account status
        - currency: Account currency
        - timezone: Account timezone
        - balance: Account balance

            advertiser_ids: A list of advertiser account IDs to retrieve information for.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successfully retrieved advertiser information

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.advertiser.info.list(advertiser_ids=["T69303382030970061B"])
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "advertiser_ids",
            to_encodable(item=advertiser_ids, dump_with=typing.List[str]),
            style="form",
            explode=False,
        )
        if not isinstance(fields, type_utils.NotGiven):
            encode_query_param(
                _query,
                "fields",
                to_encodable(
                    item=fields,
                    dump_with=typing.List[
                        typing_extensions.Literal[
                            "balance", "currency", "name", "status", "timezone"
                        ]
                    ],
                ),
                style="form",
                explode=False,
            )
        return await self._base_client.request(
            method="GET",
            path="/advertiser/info",
            auth_names=["token"],
            query_params=_query,
            cast_to=models.StandardResponse,
            request_options=request_options or default_request_options(),
        )
