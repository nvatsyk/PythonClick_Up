import requests
from faker import Faker

fake = Faker()


API_TOKEN = "pk_188684470_9R2IE4VWCYUZJGJ4U2YZ2N7XXN7ZG6MU"
TEAM_ID = "90151136171"

HEADERS = {
    "Authorization": API_TOKEN,
    "Content-Type": "application/json"
}

BASE_URL = "https://api.clickup.com/api/v2"


goal_id = None

def test_create_goal():
    global goal_id
    body = {
        "name": fake.first_name(),
        "team_id": TEAM_ID
    }
    response = requests.post(f"{BASE_URL}/team/{TEAM_ID}/goal", headers=HEADERS, json=body)
    print("Create response:", response.json())
    assert response.status_code == 200
    goal_data = response.json()["goal"]
    goal_id = goal_data["id"]
    assert goal_data["name"] == body["name"]

def test_get_created_goal():
    assert goal_id is not None
    response = requests.get(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS)
    print("Get response:", response.json())
    assert response.status_code == 200
    assert response.json()["goal"]["id"] == goal_id

def test_update_goal():
    assert goal_id is not None
    new_name = fake.last_name()
    body = {
        "name": new_name
    }
    response = requests.put(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS, json=body)
    print("Update response:", response.json())
    assert response.status_code == 200
    assert response.json()["goal"]["name"] == new_name

def test_delete_goal():
    assert goal_id is not None
    response = requests.delete(f"{BASE_URL}/goal/{goal_id}", headers=HEADERS)
    print("Delete response:", response.status_code)
    assert response.status_code == 200 or response.status_code == 204
