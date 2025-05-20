
### Get ad account details <a name="get_info"></a>

Retrieve detailed information about one or more advertising accounts.

For more details, see [Advertiser Info](https://business-api.tiktok.com/portal/docs?id=1739593083610113).


**API Endpoint**: `GET /advertiser/info`

#### Synchronous Client

```python
from os import getenv
from tiktok_business_py import Client

client = Client(api_token=getenv("API_TOKEN"))
res = client.advertiser.get_info(advertiser_ids=["T79303382030970061N"])
```

#### Asynchronous Client

```python
from os import getenv
from tiktok_business_py import AsyncClient

client = AsyncClient(api_token=getenv("API_TOKEN"))
res = await client.advertiser.get_info(advertiser_ids=["T79303382030970061N"])
```
