import requests 

def test_github_user():

    r = requests.get("https://api.github.com/users/octocat")
    assert r.status_code ==200
    assert r.json()["login"] == "octocat"