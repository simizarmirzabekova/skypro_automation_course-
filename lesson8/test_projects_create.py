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

def test_create_project_positive(api_url, auth_header):
    """Позитивный тест: создание нового проекта"""
    
    payload = {
        "name": "Test Project from API",
        "description": "Project created via pytest"
    }

    response = requests.post(
        url=f"{api_url}/projects", 
        headers=auth_header,
        json=payload
    )

    assert response.status_code == 201, \
           f"Ожидался статус 201 Created, но получен {response.status_code}"
    data = response.json()
    assert isinstance(data['id'], int), "ID созданного проекта должен быть числом"
    assert data["name"] == payload["name"], "Название проекта не совпадает с отправленным"

def test_create_project_negative_no_name(api_url, auth_header):
    """Негативный тест: попытка создать проект БЕЗ названия"""
    
    payload = {"description": "No name provided"}

    response = requests.post(f"{api_url}/projects", headers=auth_header, json=payload)

    assert response.status_code == 400, \
           f"Ожидалась ошибка 400 Bad Request, но получен {response.status_code}"
    error_data = response.json()
    assert "name" in error_data.get("errors", {}).keys(), \
       "Ошибка должна указывать на отсутствие поля name"
    