import json
from core.schema_validator import SchemaValidator

def test_list_users(user_api):
    response = user_api.list_users(page=2)
    assert response.status_code == 200
    data = response.json()
    assert data['page'] == 2
    assert len(data['data'])> 0
    assert isinstance(data['data'], list)
   

def test_craete_user(user_api):
    with open("../data/payloads/users/create_a_user.json", 'r') as file:
        payload = json.load(file)
        response = user_api.create_user(payload)


        print(f"REQUEST HEADERS: {response.request.headers}")
        print(f"Status code: {response.status_code}")

        assert response.status_code == 201
        data = response.json()

        assert data['name'] == payload['name']
        SchemaValidator.schema_validator(data, "../data/schemas/user_schema.json")
