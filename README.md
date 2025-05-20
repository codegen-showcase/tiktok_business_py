
# TikTok Business API Python SDK

## Overview
# TikTok Business API

This API allows businesses to interact with TikTok's advertising platform programmatically.

## Authentication
All endpoints require Bearer token authentication. Include your access token in the Authorization header.


#### Synchronous Client

```python
from os import getenv
from tiktok_business_py import Client

client = Client(token=getenv("API_TOKEN"))
```

#### Asynchronous Client

```python
from os import getenv
from tiktok_business_py import AsyncClient

client = AsyncClient(token=getenv("API_TOKEN"))
```

## Module Documentation and Snippets

### [adgroup.quota](tiktok_business_py/resources/adgroup/quota/README.md)

* [list](tiktok_business_py/resources/adgroup/quota/README.md#list) - Get the dynamic quota

### [advertiser.info](tiktok_business_py/resources/advertiser/info/README.md)

* [list](tiktok_business_py/resources/advertiser/info/README.md#list) - Get ad account details

<!-- MODULE DOCS END -->
