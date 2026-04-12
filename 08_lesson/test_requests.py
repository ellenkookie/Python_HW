import requests

base_url = "http://5.101.50.27:8000"

def test_simple_req():
    resp = requests.get(base_url+'/company/list?active=true')
    response_body = resp.json()
    first_company = response_body[0]
    assert first_company["name"] == "VS Code"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json"

def test_auth():
    creds = {
        "username": "bloom",
        "password": "fire-fairy"
}

    resp = requests.post(base_url + '/auth/login', json=creds)
    assert resp.status_code == 200

def test_get_companies():
    resp = requests.get(base_url+'/company/list')
    body = resp.json()

    assert resp.status_code == 200
    assert len(body) > 0