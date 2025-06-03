import requests
from faker import Faker

fake = Faker()

API_TOKEN = "pk_188684470_9R2IE4VWCYUZJGJ4U2YZ2N7XXN7ZG6MU"  # 🔒 Замінити на власний токен
TEAM_ID = "90151136171"
BASE_URL = "https://api.clickup.com/api/v2"

HEADERS = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

def test_update_goal():

    initial_name = fake.first_name()
    create_body = {
        "name": initial_name,
        "team_id": TEAM_ID
    }

    create_response = requests.post(f"{BASE_URL}/team/{TEAM_ID}/goal", headers=HEADERS, json=create_body)
    assert create_response.status_code == 200, f"Create failed: {create_response.text}"
    goal = create_response.json()["goal"]
    goal_id = goal["id"]
    print(f"Goal створено: {goal_id}, name: {initial_name}")


    updated_name = fake.last_name()
    update_body = {
        "name": updated_name
    }

    update_response = requests.put(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS, json=update_body)
    assert update_response.status_code == 200, f"Update failed: {update_response.text}"
    updated_goal = update_response.json()["goal"]
    assert updated_goal["name"] == updated_name
    print(f" Goal оновлено: нове ім’я = {updated_name}")


    get_response = requests.get(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS)
    assert get_response.status_code == 200
    assert get_response.json()["goal"]["name"] == updated_name
    print(f" Перевірка успішна: ім’я = {updated_name}")


    delete_response = requests.delete(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS)
    assert delete_response.status_code in [200, 204]
    print(f" Goal видалено: {goal_id}")
