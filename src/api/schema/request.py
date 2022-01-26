from typing import Dict, List, Union

from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    name: str = Field(..., title="Name to be displayed")
    message: str = Field(..., title="Message to be displayed along with name")


class SendOTPRequest(BaseModel):
    phone_no: str = Field(..., title="Phone no. to which we want to send OTP to")


class VerifyOTPRequest(SendOTPRequest):
    otp: str = Field(..., title="otp for the phone no.")


class UpdateUserRequest(BaseModel):
    name: str = Field(..., title="Name of the user")
    home_address: str = Field(..., title="Home address of the user")
    store_category_name: str = Field(None, title="Category name of the store")
    store_name: str = Field(None, title="Name of the Store")
    store_address: str = Field(None, title="Address of the user")
    store_description: str = Field(None, title="Description of the user")
