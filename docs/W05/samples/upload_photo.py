import os
import requests

api_base_url = os.environ.get("API_BASE_URL", "https://api.corg.ly/v1")
auth_token = os.environ.get("CORGLY_TOKEN", "your_jwt_token")

with open("einstein.jpg", "rb") as pet_photo_file:
    upload_response = requests.post(
        f"{api_base_url}/pets/upload-photo",
        headers={"Authorization": f"Bearer {auth_token}"},
        files={
            "pet_id": (None, "corgi_98231", "text/plain"),
            "photo": ("einstein.jpg", pet_photo_file, "image/jpeg"),
        },
    )

print(upload_response.status_code, upload_response.json())