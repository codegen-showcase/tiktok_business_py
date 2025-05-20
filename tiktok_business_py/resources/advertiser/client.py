from tiktok_business_py.core import AsyncBaseClient, SyncBaseClient
from tiktok_business_py.resources.advertiser.info import AsyncInfoClient, InfoClient


class AdvertiserClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.info = InfoClient(base_client=self._base_client)


class AsyncAdvertiserClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.info = AsyncInfoClient(base_client=self._base_client)
