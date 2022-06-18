import requests

response = requests.get("http://127.0.0.1:8080/",
                        headers={
                            "accept": "application/json",
                            "Content-Type": "application/json"
                        })

assert response.status_code == 200
assert response.json()["message"] == "Welcome to ŁuczniczQA API Testing app."