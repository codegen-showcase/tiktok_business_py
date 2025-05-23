
# TikTok Business API Python SDK

## Overview
# TikTok Business API

This API allows businesses to interact with TikTok's advertising platform programmatically.

## Authentication
All endpoints require Bearer token authentication. Include your access token in the Authorization header.

### FOR TIKTOK TEAM: SDK Update Demo
Check out the [SDK Update Demo](./sdk-update-demo.mov)

#### Synchronous Client

```python
from os import getenv
from tiktok_business_py import Client

client = Client(api_token=getenv("API_TOKEN"))
```

#### Asynchronous Client

```python
from os import getenv
from tiktok_business_py import AsyncClient

client = AsyncClient(api_token=getenv("API_TOKEN"))
```

## Module Documentation and Snippets

### [adgroup.quotas](tiktok_business_py/resources/adgroup/quotas/README.md)

* [get](tiktok_business_py/resources/adgroup/quotas/README.md#get) - Get the dynamic quota

### [advertiser](tiktok_business_py/resources/advertiser/README.md)

* [get_info](tiktok_business_py/resources/advertiser/README.md#get_info) - Get ad account details

<!-- MODULE DOCS END -->
