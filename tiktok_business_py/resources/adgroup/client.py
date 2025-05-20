from tiktok_business_py.core import AsyncBaseClient, SyncBaseClient
from tiktok_business_py.resources.adgroup.quotas import AsyncQuotasClient, QuotasClient


class AdgroupClient:
    def __init__(self, *, base_client: SyncBaseClient):
        self._base_client = base_client
        self.quotas = QuotasClient(base_client=self._base_client)


class AsyncAdgroupClient:
    def __init__(self, *, base_client: AsyncBaseClient):
        self._base_client = base_client
        self.quotas = AsyncQuotasClient(base_client=self._base_client)
