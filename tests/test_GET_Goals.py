import requests
from faker import Faker

fake = Faker()

valid_headers = {
    "Authorization": "pk_188684470_9R2IE4VWCYUZJGJ4U2YZ2N7XXN7ZG6MU"
}

invalid_headers = {
    "Authorization": "invalid_token"
}


def test_get_all_goals():

    result = requests.get("https://api.clickup.com/api/v2/team/90151136171/goal", headers=valid_headers)
    assert result.status_code == 200
    print("Валідний запит:", result.text)

    goals = result.json().get("goals", [])
    assert any(goal["name"] == "tuiheorutie" for goal in goals), " Не знайдено goal з ім'ям 'tuiheorutie'"

    # Запит з НЕвалідним токеном
    bad_result = requests.get("https://api.clickup.com/api/v2/team/90151136171/goal", headers=invalid_headers)
    assert bad_result.status_code in [401, 403], f"Очікувався 401/403, а отримано {bad_result.status_code}"
    print(" Помилка з невірним токеном працює як очікується:", bad_result.status_code)


