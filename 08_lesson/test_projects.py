import requests
import pytest

base_url = "https://ru.yougile.com/api-v2"
try:
    from config import LOGIN, PASSWORD, COMPANY_ID
except ImportError:
    LOGIN = "your_email@example.com"
    PASSWORD = "your_password"
    COMPANY_ID = "your_company_id"

@pytest.fixture(scope="session")
def auth_headers():
    #Получить токен
    payload = {
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": COMPANY_ID
    }

    resp = requests.post(f"{base_url}/auth/keys/get", json=payload)
    keys = resp.json()

    token = None
    for key_info in keys:
        if not key_info.get("deleted"):
            token = key_info["key"]
            break

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

# Позитивный тест: создание нового проекта
def test_create_project(auth_headers):
    payload = {
        "title": "Мой тестовый проект",
    }

    resp = requests.post(f"{base_url}/projects", json=payload, headers=auth_headers)

    assert resp.status_code == 201
    assert "id" in resp.json()

    project_id = resp.json()["id"]
    print(f"Создан проект с ID: {project_id}")


# Негативный тест: создание проекта с пустым названием
def test_create_project_empty_title(auth_headers):

    payload = {
        "title": ""
    }

    resp = requests.post(f"{base_url}/projects", json=payload, headers=auth_headers)

    # Ожидаем ошибку 400 (Bad Request)
    assert resp.status_code == 400
    assert "error" in resp.json() or "message" in resp.json()


# Позитивный тест: обновление проекта
def test_update_project_positive(auth_headers):
    create_resp = requests.post(f"{base_url}/projects", json={"title": "Для обновления"}, headers=auth_headers)
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    update_resp = requests.put(f"{base_url}/projects/{project_id}", json={"title": "Новое название"}, headers=auth_headers)
    assert update_resp.status_code == 200
    assert update_resp.json()["id"] == project_id


# Негативный тест: обновление несуществующего проекта
def test_update_project_negative(auth_headers):

    fake_id = "00000000-0000-0000-0000-000000000000"

    update_resp = requests.put(
        f"{base_url}/projects/{fake_id}",
        json={"title": "Новое название"},
        headers=auth_headers
    )

    assert update_resp.status_code == 404


# Позитивный тест: получение проекта по ID
def test_get_project_positive(auth_headers):
    create_resp = requests.post(f"{base_url}/projects", json={"title": "Для получения"}, headers=auth_headers)
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    get_resp = requests.get(f"{base_url}/projects/{project_id}", headers=auth_headers)

    assert get_resp.status_code == 200
    assert get_resp.json()["id"] == project_id
    assert get_resp.json()["title"] == "Для получения"


#Негативный тест: получение несуществующего проекта по ID
def test_get_project_negative(auth_headers):

    fake_id = "00000000-0000-0000-0000-000000000000"

    get_resp = requests.get(f"{base_url}/projects/{fake_id}", headers=auth_headers)

    assert get_resp.status_code == 404