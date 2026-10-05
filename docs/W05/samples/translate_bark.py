import os
import requests

api_base_url = os.environ.get("API_BASE_URL", "https://api.corg.ly/v1")
auth_token = os.environ.get("CORGLY_TOKEN", "your_jwt_token")

with open("einstein_bark.wav", "rb") as bark_audio_file:
    translation_response = requests.post(
        f"{api_base_url}/audio/translate-bark",
        headers={"Authorization": f"Bearer {auth_token}"},
        files={
            "audio": ("einstein_bark.wav", bark_audio_file, "audio/wav"),
            "language": (None, "en", "text/plain"),
        },
    )

print(translation_response.status_code, translation_response.json())