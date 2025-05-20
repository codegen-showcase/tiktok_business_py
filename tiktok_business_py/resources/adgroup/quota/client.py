import typing

from tiktok_business_py.core import (
    AsyncBaseClient,
    QueryParams,
    RequestOptions,
    SyncBaseClient,
    default_request_options,
    encode_query_param,
    to_encodable,
)
from tiktok_business_py.types import models


class QuotaClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client

    def list(
        self,
        *,
        advertiser_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.StandardResponse:
        """
        Get the dynamic quota

        Use this endpoint to get the dynamic quota on the number of active auction ad groups that an advertiser can have.

        For more details, see [Adgroup Quota](https://ads.tiktok.com/marketing_api/docs?id=1768463039162369).


        GET /adgroup/quota

        Args:
            advertiser_id: The unique identifier of the advertiser account.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successfully retrieved quota information

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        client.adgroup.quota.list(advertiser_id="T69303382030970061B")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "advertiser_id",
            to_encodable(item=advertiser_id, dump_with=str),
            style="form",
            explode=True,
        )
        return self._base_client.request(
            method="GET",
            path="/adgroup/quota",
            auth_names=["token"],
            query_params=_query,
            cast_to=models.StandardResponse,
            request_options=request_options or default_request_options(),
        )


class AsyncQuotaClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client

    async def list(
        self,
        *,
        advertiser_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> models.StandardResponse:
        """
        Get the dynamic quota

        Use this endpoint to get the dynamic quota on the number of active auction ad groups that an advertiser can have.

        For more details, see [Adgroup Quota](https://ads.tiktok.com/marketing_api/docs?id=1768463039162369).


        GET /adgroup/quota

        Args:
            advertiser_id: The unique identifier of the advertiser account.
            request_options: Additional options to customize the HTTP request

        Returns:
            Successfully retrieved quota information

        Raises:
            ApiError: A custom exception class that provides additional context
                for API errors, including the HTTP status code and response body.

        Examples:
        ```py
        await client.adgroup.quota.list(advertiser_id="T69303382030970061B")
        ```
        """
        _query: QueryParams = {}
        encode_query_param(
            _query,
            "advertiser_id",
            to_encodable(item=advertiser_id, dump_with=str),
            style="form",
            explode=True,
        )
        return await self._base_client.request(
            method="GET",
            path="/adgroup/quota",
            auth_names=["token"],
            query_params=_query,
            cast_to=models.StandardResponse,
            request_options=request_options or default_request_options(),
        )
