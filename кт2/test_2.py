import json
import pytest

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def test_superheroes_age():
    data = load_data('superhero_new.json')
    
    for member in data['members']:
        assert member['age'] > 33, f"{member['name']} is not older than 33 years"
