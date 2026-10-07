import requests 
r = requests.get("https://api.github.com/users/octocat")
print(r.status_code)
print(r.json()["login"])