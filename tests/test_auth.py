def test_register_and_login(http):
    r = http.post("/auth/register", json={"email": "x@y.com", "password": "Pass123!"})
    assert r.status_code == 201
    r2 = http.post("/auth/login", data={"username": "x@y.com", "password": "Pass123!"}, headers={"Content-Type": "application/x-www-form-urlencoded"})
    assert r2.status_code == 200
    assert "access_token" in r2.json()
