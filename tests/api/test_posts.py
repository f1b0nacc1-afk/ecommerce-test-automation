import allure
import pytest


@allure.feature("JSONPlaceholder API")
@allure.story("Posts")
@pytest.mark.api
class TestPostsAPI:
    @allure.title("Get posts by user id")
    @pytest.mark.smoke
    def test_get_posts_by_user(self, api_client):
        response = api_client.get("/posts", params={"userId": 1})

        assert response.status_code == 200
        posts = response.json()
        assert len(posts) > 0
        assert all(post["userId"] == 1 for post in posts)

    @allure.title("Get single post by id")
    def test_get_post_by_id(self, api_client):
        response = api_client.get("/posts/1")

        assert response.status_code == 200
        post = response.json()
        assert post["id"] == 1
        assert post["title"]
        assert post["body"]

    @allure.title("Update post")
    def test_update_post(self, api_client):
        payload = {"id": 1, "title": "Updated title", "body": "Updated body", "userId": 1}
        response = api_client.put("/posts/1", json=payload)

        assert response.status_code == 200
        body = response.json()
        assert body["title"] == payload["title"]
        assert body["body"] == payload["body"]

    @allure.title("Delete post")
    def test_delete_post(self, api_client):
        response = api_client.delete("/posts/1")

        assert response.status_code == 200
