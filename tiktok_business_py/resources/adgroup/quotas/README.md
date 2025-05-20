
### Get the dynamic quota <a name="get"></a>

Use this endpoint to get the dynamic quota on the number of active auction ad groups that an advertiser can have.

For more details, see [Adgroup Quota](https://ads.tiktok.com/marketing_api/docs?id=1768463039162369).


**API Endpoint**: `GET /adgroup/quota`

#### Synchronous Client

```python
from os import getenv
from tiktok_business_py import Client

client = Client(api_token=getenv("API_TOKEN"))
res = client.adgroup.quotas.get(advertiser_id="6793033820309700610")
```

#### Asynchronous Client

```python
from os import getenv
from tiktok_business_py import AsyncClient

client = AsyncClient(api_token=getenv("API_TOKEN"))
res = await client.adgroup.quotas.get(advertiser_id="6793033820309700610")
```
