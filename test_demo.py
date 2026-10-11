import requests 

def test_github_user():

    r = requests.get("https://api.github.com/users/octocat")
    assert r.status_code ==200
    assert r.json()["login"] == "octocat"


def test_github_user_not_found():

    r = requests.get("https//api.github.com/user/this_user_does_not_exist_12345")
    assert r.status_code == 404
    assert r.json()["message"] == "not found"
    print("返回的错误信息是：", r.json()["message"])
