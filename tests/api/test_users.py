import allure
import pytest


@allure.feature("JSONPlaceholder API")
@allure.story("Users")
@pytest.mark.api
class TestUsersAPI:
    @allure.title("Get list of users")
    @pytest.mark.smoke
    def test_get_users_list(self, api_client):
        response = api_client.get("/users")

        assert response.status_code == 200
        users = response.json()
        assert len(users) == 10
        assert "email" in users[0]
        assert "@" in users[0]["email"]

    @allure.title("Get single user by id")
    def test_get_user_by_id(self, api_client):
        response = api_client.get("/users/1")

        assert response.status_code == 200
        user = response.json()
        assert user["id"] == 1
        assert user["name"]
        assert "@" in user["email"]

    @allure.title("Create user")
    def test_create_user(self, api_client):
        payload = {
            "name": "QA Tester",
            "username": "qa_tester",
            "email": "qa@example.com",
        }
        response = api_client.post("/users", json=payload)

        assert response.status_code == 201
        body = response.json()
        assert body["name"] == payload["name"]
        assert body["email"] == payload["email"]
        assert "id" in body
