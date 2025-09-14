# order/utils.py
import requests

def get_user_from_user_service(user_id, token):
    try:
        response = requests.get(
            f"http://user-service:8001/api/auth/users/{user_id}/",
            headers={"Authorization": f"Bearer {token}"},
            timeout=5
        )
        return response.status_code == 200
    except:
        return False