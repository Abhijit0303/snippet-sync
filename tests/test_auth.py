def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "password123"
            },
    )

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"

def test_register_duplicate_user(client):
    client.post(
        "/auth/register",
        json={
            "email": "dup@example.com",
            "password": "password123",
        },
    )

    response = client.post(
        "/auth/register",
        json={
            "email": "dup@example.com",
            "password": "password123",
        },
    )

    assert response.status_code in (400, 409)

def test_login_user(client):
    register_response = client.post(
        "/auth/register",
        json={
            "email": "login_test@example.com",
            "password": "password123",
        },
    )
    assert register_response.status_code == 200

    login_response = client.post(
        "/auth/login",
        data={
            "username": "login_test@example.com",
            "password": "password123",
        },
    )

    assert login_response.status_code == 200
    data = login_response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_wrong_password(client):
    client.post(
        "/auth/register",
        json={
            "email": "wrong_pass@example.com",
            "password": "password123",
        },
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "wrong_pass@example.com",
            "password": "wrongpassword",
        },
    )

    assert response.status_code == 401


def test_login_nonexistent_user(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "ghost@example.com",
            "password": "ghostpassword",
        },
    )

    assert response.status_code == 401
