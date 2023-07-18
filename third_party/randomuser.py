import requests
from bs4 import BeautifulSoup

def get_random_user():
    response = requests.get("https://randomuser.me/api/")
    if response.status_code == 200:
        data = response.json()
        return data['results'][0]
    else:
        return None

def parse_user_info(user):
    parsed_info = {}
    parsed_info['name'] = user['name']['first'] + ' ' + user['name']['last']
    parsed_info['email'] = user['email']
    parsed_info['username'] = user['login']['username']
    parsed_info['gender'] = user['gender']
    # Add more fields as per your requirements
    return parsed_info

if __name__ == "__main__":
    user = get_random_user()
    if user:
        parsed_info = parse_user_info(user)
        print(parsed_info)
    else:
        print("Error retrieving user information.")
