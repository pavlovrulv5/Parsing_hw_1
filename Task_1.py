import requests
import json

url = 'https://api.github.com/'

user = input('Введите имя пользователя: ')

link = f'{url}users/{user}/repos'

response = requests.get(link)
res = json.loads(response.text)

if response.ok:
    for n in res:
        print('Список репозиториев:')
        print(n['name'])

with open('data.json', 'w') as file:
    json.dump(res, file, indent=2, ensure_ascii=False)
