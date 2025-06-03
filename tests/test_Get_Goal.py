import requests
from faker import Faker

fake = Faker()


API_TOKEN = "pk_188684470_9R2IE4VWCYUZJGJ4U2YZ2N7XXN7ZG6MU"  # заміни на свій токен
TEAM_ID = "90151136171"
BASE_URL = "https://api.clickup.com/api/v2"

HEADERS = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

def test_get_goal_by_id():

    goal_name = fake.first_name()
    body = {
        "name": goal_name,
        "team_id": TEAM_ID
    }

    create_response = requests.post(f"{BASE_URL}/team/{TEAM_ID}/goal", headers=HEADERS, json=body)
    assert create_response.status_code == 200, f"Create failed: {create_response.text}"
    goal = create_response.json()["goal"]
    goal_id = goal["id"]


    get_response = requests.get(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS)
    assert get_response.status_code == 200, f"Get failed: {get_response.text}"
    goal_data = get_response.json()["goal"]


    assert goal_data["id"] == goal_id
    assert goal_data["name"] == goal_name

    print(f"✅ Goal отримано успішно: ID = {goal_id}, name = {goal_name}")


    delete_response = requests.delete(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS)
    assert delete_response.status_code in [200, 204], f"Delete failed: {delete_response.text}"
    print(f"🗑 Goal успішно видалено: {goal_id}")
