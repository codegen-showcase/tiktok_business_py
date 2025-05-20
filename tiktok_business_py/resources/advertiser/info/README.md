
### Get ad account details <a name="list"></a>

Retrieve detailed information about one or more advertising accounts.

For more details, see [Advertiser Info](https://business-api.tiktok.com/portal/docs?id=1739593083610113).


**API Endpoint**: `GET /advertiser/info`

#### Synchronous Client

```python
from os import getenv
from tiktok_business_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.advertiser.info.list(advertiser_ids=["T69303382030970061B"])
```

#### Asynchronous Client

```python
from os import getenv
from tiktok_business_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.advertiser.info.list(advertiser_ids=["T69303382030970061B"])
```
