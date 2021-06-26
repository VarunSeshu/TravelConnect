from typing import List, Literal, Union

from pydantic import BaseModel, Field


class ResponseModel(BaseModel):
    return_message: str = Field(..., title="Message from the server")
