import requests

database = {
    1: "Anvitha",
    2: "Siri",
    3: "Jai"
            }


def get_user_from_db(user_id):
    return database.get(user_id)


def get_users():
    reponse = requests.get("https://jsonplaceholder.typicode.com/users")
    if reponse.status_code == 200:
        return reponse.json()

    raise requests.HTTPError