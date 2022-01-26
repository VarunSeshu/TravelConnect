import cloudinary
from src.config import env


class Cloudinary:
    def __init__(self):
        cloudinary.config(
            cloud_name=env.CLOUDINARY_CLOUD_NAME,
            api_key=env.CLOUDINARY_API_KEY,
            api_secret=env.CLOUDINARY_API_SECRET,
        )

    def get_cloud_url(self, image):
        response = cloudinary.uploader.upload("")

        return response["url"]
