class USER_API:
    def __init__(self, client):
        self.client = client

    def get_user(self, user_id):
        return self.client.get(f"api/users/{user_id}")
    
    def get_all_users(self):
        return self.client.get("api/users")
    
    def list_users(self, page):
        return self.client.get(f"api/users?page={page}")
    
    def create_user(self, payload):
        return self.client.post(f"api/users", json=payload)