from typing import Dict, List, Union

from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    name: str = Field(..., title="Name to be displayed")
    message: str = Field(..., title="Message to be displayed along with name")
