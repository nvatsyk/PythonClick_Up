import requests
from faker import Faker

fake = Faker()

API_TOKEN = "pk_188684470_9R2IE4VWCYUZJGJ4U2YZ2N7XXN7ZG6MU"  # 🔐 Заміни на свій
TEAM_ID = "90151136171"
BASE_URL = "https://api.clickup.com/api/v2"

HEADERS = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

def test_delete_goal():

    goal_name = fake.first_name()
    body = {
        "name": goal_name,
        "team_id": TEAM_ID
    }

    create_response = requests.post(f"{BASE_URL}/team/{TEAM_ID}/goal", headers=HEADERS, json=body)
    assert create_response.status_code == 200, f"Create failed: {create_response.text}"
    goal = create_response.json()["goal"]
    goal_id = goal["id"]
    print(f"✅ Створено Goal: {goal_id}, name: {goal_name}")


    delete_response = requests.delete(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS)
    assert delete_response.status_code in [200, 204], f"Delete failed: {delete_response.text}"
    print(f"🗑 Видалено Goal: {goal_id}")


    get_response = requests.get(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS)
    assert get_response.status_code != 200, f"Goal не мав існувати: {get_response.text}"
    print("❌ Goal більше не існує — перевірка пройдена")
