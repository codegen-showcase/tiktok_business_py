
# TikTok Business API Python SDK

## Overview
# TikTok Business API

This API allows businesses to interact with TikTok's advertising platform programmatically.

## Authentication
All endpoints require Bearer token authentication. Include your access token in the Authorization header.

### FOR TIKTOK TEAM: SDK Update Demo
<video src="https://github.com/codegen-showcase/tiktok_business_py/blob/main/sdk-update-demo.mov" width="640" height="360" controls></video>

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

### [adgroup.quotas](tiktok_business_py/resources/adgroup/quotas/README.md)

* [get](tiktok_business_py/resources/adgroup/quotas/README.md#get) - Get the dynamic quota

### [advertiser](tiktok_business_py/resources/advertiser/README.md)

* [get_info](tiktok_business_py/resources/advertiser/README.md#get_info) - Get ad account details

<!-- MODULE DOCS END -->
