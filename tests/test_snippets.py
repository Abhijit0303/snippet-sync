def get_auth_headers(client):
    # Ensure user exists
    client.post(
        "/auth/register",
        json={
            "email": "snippet_user@example.com",
            "password": "test123",
        },
    )

    # Login
    login_response = client.post(
        "/auth/login",
        data={
            "username": "snippet_user@example.com",
            "password": "test123",
        },
    )

    assert login_response.status_code == 200

    token = login_response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_snippet(client):
    headers = get_auth_headers(client)

    response = client.post(
        "/snippets/add",
        json={
            "title": "Test Snippet",
            "content": "print('hello')",
            "language": "python",
            "tags": "test",
        },
        headers=headers,
    )

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Snippet"
    assert data["language"] == "python"

def test_create_snippet_without_token(client):
    response = client.post(
        "/snippets/add",
        json={
            "title": "No Token",
            "content": "print('fail')",
            "language": "python",
        },
    )

    assert response.status_code == 401


def test_get_nonexistent_snippet(client):
    headers = get_auth_headers(client)

    response = client.get(
        "/snippets/does-not-exist",
        headers=headers,
    )

    assert response.status_code == 404
