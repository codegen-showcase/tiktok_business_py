from tiktok_business_py.core import AsyncBaseClient, SyncBaseClient
from tiktok_business_py.resources.adgroup.quota import AsyncQuotaClient, QuotaClient


class AdgroupClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.quota = QuotaClient(base_client=self._base_client)


class AsyncAdgroupClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.quota = AsyncQuotaClient(base_client=self._base_client)
