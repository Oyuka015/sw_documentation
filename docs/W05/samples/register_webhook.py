import os
import requests

api_base_url = os.environ.get("API_BASE_URL", "https://api.corg.ly/v1")
auth_token = os.environ.get("CORGLY_TOKEN", "your_jwt_token")

subscription_response = requests.post(
    f"{api_base_url}/webhooks/subscribe",
    headers={"Authorization": f"Bearer {auth_token}"},
    json={
        "callback_url": "https://myapp.example.com/hooks/corgly",
        "events": ["pet.photo_uploaded", "bark.translated"],
    },
)

print(subscription_response.status_code, subscription_response.json())