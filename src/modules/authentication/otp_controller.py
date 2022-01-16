from xmlrpc.client import Boolean
from twilio.rest import Client

from src.config import env
import logging

logger = logging.getLogger("backend")


class OtpController:
    def __init__(self, phone_no):
        self.phone_no = f"+91{phone_no}"
        self.client = Client(env.ACCOUNT_SID, env.AUTH_TOKEN)
        self.sid = env.SID

    def send_otp(self):
        try:
            self.client.verify.services(self.sid).verifications.create(
                to=self.phone_no, channel="sms"
            )
            return True
        except Exception:
            return False

    def verify_otp(self, otp):
        try:
            verification_check = self.client.verify.services(
                self.sid
            ).verification_checks.create(to=self.phone_no, code=otp)
            if verification_check.status == "approved":
                return True
            return False
        except Exception as e:
            logger.exception(f"Exception occurred while verifying user with otp.")
            return False
