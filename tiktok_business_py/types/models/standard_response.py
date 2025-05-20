import pydantic
import typing


class StandardResponse(pydantic.BaseModel):
    """
    Standard API response structure used across all endpoints
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    code: int = pydantic.Field(
        alias="code",
    )
    """
    Response code. 0 indicates success, other values indicate errors.
    For the complete list of response codes and descriptions, see 
    [Return Codes](https://ads.tiktok.com/marketing_api/docs?id=1737172488964097).
    
    """
    data: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="data", default=None
    )
    """
    The operation's returned data.
    """
    message: str = pydantic.Field(
        alias="message",
    )
    """
    Response message providing details about the result of the operation.
    """
    request_id: str = pydantic.Field(
        alias="request_id",
    )
    """
    The log ID of a request, which uniquely identifies the request.
    """
