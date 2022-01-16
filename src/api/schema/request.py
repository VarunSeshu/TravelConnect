from typing import Dict, List, Union

from pydantic import BaseModel, Field


class RequestModel(BaseModel):
    name: str = Field(..., title="Name to be displayed")
    message: str = Field(..., title="Message to be displayed along with name")


class SendOTPRequest(BaseModel):
    phone_no: str = Field(..., title="Phone no. to which we want to send OTP to")


class VerifyOTPRequest(SendOTPRequest):
    otp: str = Field(..., title="otp for the phone no.")
