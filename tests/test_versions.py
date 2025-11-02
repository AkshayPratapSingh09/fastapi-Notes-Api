def auth(http):
    http.post("/auth/register", json={"email": "v@v.com", "password": "Pass123!"})
    r = http.post("/auth/login", data={"username": "v@v.com", "password": "Pass123!"}, headers={"Content-Type": "application/x-www-form-urlencoded"})
    token = r.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_versions_flow(http):
    h = auth(http)
    r = http.post("/notes/", json={"title": "T1", "content": "C1"}, headers=h)
    nid = r.json()["id"]
    http.patch(f"/notes/{nid}", json={"content": "C2"}, headers=h)
    http.patch(f"/notes/{nid}", json={"content": "C3"}, headers=h)
    v = http.get(f"/notes/{nid}/versions/", headers=h)
    assert v.status_code == 200
    assert len(v.json()) >= 3
    one = http.get(f"/notes/{nid}/versions/1", headers=h)
    assert one.status_code == 200
    res = http.post(f"/notes/{nid}/versions/1/restore", headers=h)
    assert res.status_code == 200
