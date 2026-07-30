import os
import requests
import pytest


@pytest.fixture(scope='session')
def api_url():
    """Возвращает URL сервиса."""
    return 'https://yougile.ru/api-v2'


@pytest.fixture(scope='session', autouse=True)
def auth_header():
    """
    Возвращает заголовок Authorization с токеном,
    который берётся из переменной окружения.
    """
    token = os.getenv('YOUGILE_TOKEN')  # Читаем из .env
    if not token:
        raise ValueError("Не найден токен YOUGILE_TOKEN")
    return {'Authorization': f'Bearer {token}'}

# Фикстуры уже есть выше

@pytest.fixture(scope="function")
def temp_project_id(api_url, auth_header):
    """
    Создаёт новый проект перед запуском теста
    и возвращает его ID. После завершения теста удаляет его.
    """
    create_payload = {"name": "Temp Test Project"}
    resp_create = requests.post(f"{api_url}/projects", headers=auth_header, json=create_payload)
    project_id = resp_create.json()["id"]

    yield project_id  # Передаём ID в тест

    # Удаление после выполнения теста
    delete_resp = requests.delete(f"{api_url}/projects/{project_id}", headers=auth_header)
    assert delete_resp.status_code < 400, "Не удалось удалить временный проект!"


def test_get_project_positive(temp_project_id, api_url, auth_header):
    """Позитивный тест: получение информации о существующем проекте"""
    
    response = requests.get(
        url=f"{api_url}/projects/{temp_project_id}",
        headers=auth_header
    )

    assert response.status_code == 200, \
           f"Ожидался статус 200 OK, но получен {response.status_code}"
    data = response.json()
    assert isinstance(data['id'], int), "ID проекта должен быть числом"


def test_put_project_positive(temp_project_id, api_url, auth_header):
    """Позитивный тест: обновление описания проекта"""
    
    update_payload = {"description": "Updated description via pytest"}

    response = requests.put(
        url=f"{api_url}/projects/{temp_project_id}",
        headers=auth_header,
        json=update_payload
    )

    assert response.status_code == 200, \
           f"Ожидался статус 200 OK, но получен {response.status_code}"

    # Проверяем изменения сразу же
    get_resp = requests.get(f"{api_url}/projects/{temp_project_id}", headers=auth_header)
    updated_data = get_resp.json()
    assert updated_data["description"] == update_payload["description"], \
           "Описание не изменилось после обновления"


def test_get_nonexistent_project_negative(api_url, auth_header):
    """Негативный тест: чтение НЕСУЩЕСТВУЮЩЕГО проекта"""
    
    non_existent_id = 999999999

    response = requests.get(
        url=f"{api_url}/projects/{non_existent_id}",
        headers=auth_header
    )

    assert response.status_code == 404, \
           f"Ожидалась ошибка 404 Not Found, но получен {response.status_code}"
    