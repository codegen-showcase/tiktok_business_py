import httpx
import typing

from tiktok_business_py.core import AsyncBaseClient, AuthBearer, SyncBaseClient
from tiktok_business_py.environment import Environment, _get_base_url
from tiktok_business_py.resources.adgroup import AdgroupClient, AsyncAdgroupClient
from tiktok_business_py.resources.advertiser import (
    AdvertiserClient,
    AsyncAdvertiserClient,
)


class Client:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.PRODUCTION,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = SyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.Client(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("token", AuthBearer(val=token))
        self.adgroup = AdgroupClient(base_client=self._base_client)
        self.advertiser = AdvertiserClient(base_client=self._base_client)


class AsyncClient:
    def __init__(
        self,
        *,
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        base_url: typing.Optional[str] = None,
        environment: Environment = Environment.PRODUCTION,
        token: typing.Optional[str] = None,
    ):
        """Initialize root client"""
        self._base_client = AsyncBaseClient(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            httpx_client=httpx.AsyncClient(timeout=timeout)
            if httpx_client is None
            else httpx_client,
        )
        self._base_client.register_auth("token", AuthBearer(val=token))
        self.adgroup = AsyncAdgroupClient(base_client=self._base_client)
        self.advertiser = AsyncAdvertiserClient(base_client=self._base_client)
