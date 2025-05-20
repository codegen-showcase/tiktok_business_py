
### Get the dynamic quota <a name="list"></a>

Use this endpoint to get the dynamic quota on the number of active auction ad groups that an advertiser can have.

For more details, see [Adgroup Quota](https://ads.tiktok.com/marketing_api/docs?id=1768463039162369).


**API Endpoint**: `GET /adgroup/quota`

#### Synchronous Client

```python
from os import getenv
from tiktok_business_py import Client

client = Client(token=getenv("API_TOKEN"))
res = client.adgroup.quota.list(advertiser_id="T69303382030970061B")
```

#### Asynchronous Client

```python
from os import getenv
from tiktok_business_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
res = await client.adgroup.quota.list(advertiser_id="T69303382030970061B")
```
