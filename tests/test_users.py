def user_payload(uid=1, name="paul", email="paul@atu.ie", age=26, student_id="1234567"):
    return {
        "user_id": uid,
        "name": name,
        "email": email,
        "age": age,
        "student_id": student_id
    }


def test_create_user_returns_201(client):
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["user_id"] == 1
    assert data["name"] == "paul"
    assert data["email"] == "paul@atu.ie"
    assert data["age"] == 26
    assert data["student_id"] == "1234567"


def test_duplicate_user_id_returns_409(client):
    client.post("/api/users", json=user_payload(uid=2))
    response = client.post("/api/users", json=user_payload(uid=2))

    assert response.status_code == 409
    assert "exists" in response.json()["detail"].lower()
