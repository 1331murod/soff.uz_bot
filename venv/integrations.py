import requests





def get_refferall(username, password):
    url = "https://api.soff.uz/auth/login/"

    data = {
        "phone_or_email": username,
        "password": password
    }

    response = requests.post(url=url, data=data)

    if response.status_code == 200:
        data = response.json()
        token = data['access']

        url = "https://api.soff.uz/auth/profile/"
        headers = {
            'Authorization': f'Bearer {token}' 
        }
        response = requests.get(url=url, headers=headers)
        text = f"https://soff.uz/account/register/{response.json()['code']}"
        return text



