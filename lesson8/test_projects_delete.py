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
def another_temp_project_id(api_url, auth_header):
    """
    Ещё одна фикстура временного проекта.
    Нужна отдельно, чтобы не мешаться с предыдущими тестами.
    """
    create_payload = {"name": "Another Temp Project for Delete"}
    resp_create = requests.post(f"{api_url}/projects", headers=auth_header, json=create_payload)
    project_id = resp_create.json()["id"]

    yield project_id  # Передаём ID в тест


def test_delete_project_positive(another_temp_project_id, api_url, auth_header):
    """Позитивный тест: успешное удаление проекта"""
    
    response = requests.delete(
        url=f"{api_url}/projects/{another_temp_project_id}",
        headers=auth_header
    )

    assert response.status_code == 200, \
           f"Ожидался статус 200 OK, но получен {response.status_code}"

    # Попробуем прочитать удалённый проект
    read_after_del = requests.get(
        url=f"{api_url}/projects/{another_temp_project_id}",
        headers=auth_header
    )
    assert read_after_del.status_code == 404, "Проект всё ещё доступен после удаления!"
    