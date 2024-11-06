import os
import pytest
from tasks import get_string_length, save_string_to_file, create_connection, clear_database

@pytest.fixture
def string_length_test_cases():
    return {
        "empty_string": "",
        "single_line": "Hello, World!",
        "multiline": "Hello,\nWorld!",
        "spaces_only": "   ",
    }

@pytest.fixture
def file_path(tmpdir):
    return tmpdir.join("test_file.txt")

@pytest.fixture
def db_connection(tmpdir):
    db_path = tmpdir.join("test.db")
    conn = create_connection(db_path)
    yield conn
    clear_database(conn)
    conn.close()



# 1
def test_get_string_length(string_length_test_cases):
    for key, value in string_length_test_cases.items():
        assert get_string_length(value) == len(value), f"Тест провален для {key}"

# Ожидаемый провал
def test_get_string_length_fail():
    assert get_string_length("Hello") == 6, "Тест провален: ожидалась длина 6"

# 2 
def test_save_string_to_file(file_path):
    test_string = "Hello, World!"
    save_string_to_file(test_string, file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    assert content == test_string, "Содержимое файла не соответствует ожидаемой строке"

# Ожидаемый провал
def test_save_string_to_file_fail(file_path):
    test_string = "Hello, World!"
    save_string_to_file(test_string, file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    assert content == "Hello, Python!", "Тест провален: ожидалась строка 'Hello, Python!'"

# 3 
def test_db_connection(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO test_table (name) VALUES ('test_name');")
    db_connection.commit()

    cursor.execute("SELECT * FROM test_table;")
    rows = cursor.fetchall()
    assert len(rows) == 1, "Вставка данных провалилась"
    assert rows[0][1] == 'test_name', "Получение данных провалилось"

# Ожидаемый провал
def test_db_connection_fail(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO test_table (name) VALUES ('test_name');")
    db_connection.commit()

    cursor.execute("SELECT * FROM test_table;")
    rows = cursor.fetchall()
    assert len(rows) == 0, "Тест провален: ожидалось 0 строк"