import pydantic
import pytest

from tiktok_business_py import AsyncClient, Client
from tiktok_business_py.environment import Environment
from tiktok_business_py.types import models


def test_get_info_200_generated_success():
    """Tests a GET request to the /advertiser/info endpoint.

    Operation: get_info
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Synchronous execution

    Response : models.StandardResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling sync method with example data
    client = Client(api_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = client.advertiser.get_info(advertiser_ids=["6793033820309700610"])
    try:
        pydantic.TypeAdapter(models.StandardResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"


@pytest.mark.asyncio
async def test_await_get_info_200_generated_success():
    """Tests a GET request to the /advertiser/info endpoint.

    Operation: get_info
    Test Case ID: generated_success
    Expected Status: 200
    Mode: Asynchronous execution

    Response : models.StandardResponse

    Validates:
    - Authentication requirements are satisfied
    - All required input parameters are properly handled
    - Response status code is correct
    - Response data matches expected schema

    This test uses example data to verify the endpoint behavior.
    """
    # tests calling async method with example data
    client = AsyncClient(api_token="API_TOKEN", environment=Environment.MOCK_SERVER)
    response = await client.advertiser.get_info(advertiser_ids=["6793033820309700610"])
    try:
        pydantic.TypeAdapter(models.StandardResponse).validate_python(response)
        is_json = True
    except pydantic.ValidationError:
        is_json = False
    assert is_json, "failed response type check"
