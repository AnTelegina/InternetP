import requests
import sys

with open('access_token.txt', 'r') as file:
    token = file.readline()
version = 5.95
user_id = sys.argv[1]
fields = 'nickname'
namecase = 'name_case'
count = 0

response = requests.get('https://api.vk.com/method/friends.get',
                        params={
                            'access_token': token,
                            'v': version,
                            'user_id': user_id,
                            'fields': fields,
                            'name_case': namecase
                             }
                        )

data = response.json()['response']['items']

print('Колличество друзей:', len(data), "\n")

for number in range(len(data)):
    if data[number]['online'] != 0:
        count += 1
        print('id пользователя:', data[number]['id'], '\n'
              + 'Имя пользователя:', data[number]['first_name'], '\n'
              + 'Фамилия пользователя:', data[number]['last_name'], '\n'
              + '________________', "\n")

print("Количество друзей в сети:", count)
