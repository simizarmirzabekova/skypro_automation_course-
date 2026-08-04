import pytest
from sqlalchemy import text

def test_add_student(db_session):
    # 1. Вставляем нового студента через сырой SQL, но через SQLAlchemy (Core)
    # Мы используем RETURNING id, чтобы узнать ID добавленной записи
    result = db_session.execute(
        text("INSERT INTO students (name, age, email) VALUES ('Ivan Petrov', 22, 'ivan@example.com') RETURNING id")
    )
    new_id = result.fetchone()[0]
    db_session.commit() # Фиксируем изменения в БД
    
    # 2. Проверяем, что студент появился (Ищем его по ID)
    student = db_session.execute(
        text("SELECT name, age, email FROM students WHERE id = :id"),
        {"id": new_id}
    ).fetchone()
    
    assert student is not None, "Студент не был добавлен!"
    assert student.name == "Ivan Petrov"
    assert student.age == 22
    
    # 3. Очистка (Удаляем созданного студента, чтобы тест был стабильным)
    db_session.execute(text("DELETE FROM students WHERE id = :id"), {"id": new_id})
    db_session.commit()


def test_update_student(db_session):
    # 1. Сначала создадим студента, которого будем менять
    result = db_session.execute(
        text("INSERT INTO students (name, age, email) VALUES ('Old Name', 20, 'old@example.com') RETURNING id")
    )
    new_id = result.fetchone()[0]
    db_session.commit()
    
    # 2. Обновляем его возраст
    db_session.execute(
        text("UPDATE students SET age = 30, name = 'New Name' WHERE id = :id"),
        {"id": new_id}
    )
    db_session.commit()
    
    # 3. Проверяем, что данные изменились
    student = db_session.execute(
        text("SELECT name, age FROM students WHERE id = :id"),
        {"id": new_id}
    ).fetchone()
    
    assert student.name == "New Name"
    assert student.age == 30
    
    # 4. Очистка (Удаляем созданного студента)
    db_session.execute(text("DELETE FROM students WHERE id = :id"), {"id": new_id})
    db_session.commit()


def test_delete_student(db_session):
    # 1. Сначала создадим студента для удаления
    result = db_session.execute(
        text("INSERT INTO students (name, age, email) VALUES ('To Delete', 99, 'delete@example.com') RETURNING id")
    )
    new_id = result.fetchone()[0]
    db_session.commit()
    
    # 2. Удаляем его
    db_session.execute(text("DELETE FROM students WHERE id = :id"), {"id": new_id})
    db_session.commit()
    
    # 3. Проверяем, что его больше нет
    student = db_session.execute(
        text("SELECT id FROM students WHERE id = :id"),
        {"id": new_id}
    ).fetchone()
    
    assert student is None, "Студент не был удален!"
    