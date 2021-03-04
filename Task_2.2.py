import csv
import requests



def take_100_posts():
    token = 'd674a0acd674a0acd674a0ac3cd6021a22dd674d674a0acb635e364baa8de93d5c51470'
    version = 5.126
    domain = 'typicalboxer'
    count = 100
    offset = 10
    all_posts = []

    while offset < 100:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(data):
    with open('typicalboxer.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('likes', 'body', 'url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass
            a_pen.writerow((post['likes']['count'], post['short_text_rate'], img_url))

all_posts = take_100_posts()
file_writer(all_posts)
