import json

# Шаг 1: Загрузка данных из JSON файла
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Шаг 2: Добавление новых супергероев
def add_superheroes(data):
    new_heroes = [
        {
            "name": "Captain Marvel",
            "age": 33,
            "secretIdentity": "Carol Danvers",
            "powers": [
                "Superhuman strength",
                "Flight",
                "Energy projection"
            ]
        },
        {
            "name": "Spider-Man",
            "age": 18,
            "secretIdentity": "Peter Parker",
            "powers": [
                "Superhuman agility",
                "Spider-sense",
                "Wall-crawling"
            ]
        }
    ]
    data['members'].extend(new_heroes)

# Шаг 3: Сортировка по возрасту
def sort_superheroes(data):
    data['members'].sort(key=lambda x: x['age'])

# Шаг 4: Запись в новый JSON файл
def save_data(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Основная функция
def main():
    input_file = 'SuperHero.json' 
    output_file = 'SuperHero_new.json' 

    # Загрузка данных
    data = load_data(input_file)

    # Добавление новых супергероев
    add_superheroes(data)

    # Сортировка по возрасту
    sort_superheroes(data)

    # Сохранение результата
    save_data(output_file, data)

if __name__ == '__main__':
    main()
