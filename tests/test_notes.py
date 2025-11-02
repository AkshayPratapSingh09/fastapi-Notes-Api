def auth(http):
    http.post("/auth/register", json={"email": "a@b.com", "password": "Pass123!"})
    r = http.post("/auth/login", data={"username": "a@b.com", "password": "Pass123!"}, headers={"Content-Type": "application/x-www-form-urlencoded"})
    token = r.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_create_list_get_delete_note(http):
    h = auth(http)
    r = http.post("/notes/", json={"title": "T", "content": "C"}, headers=h)
    assert r.status_code == 201
    nid = r.json()["id"]
    r2 = http.get("/notes/", headers=h)
    assert r2.status_code == 200
    r3 = http.get(f"/notes/{nid}", headers=h)
    assert r3.status_code == 200
    r4 = http.delete(f"/notes/{nid}", headers=h)
    assert r4.status_code == 204
