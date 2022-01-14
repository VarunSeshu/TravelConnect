from os import access
from typing import List, Literal, Union

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    return_message: str = Field(..., title="Message from the server")


class LoginResponse(BaseModel):
    success: bool = Field(..., title="Success status of Login API")
    access_token: str = Field(None, title="Access token for the user")
