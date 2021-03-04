from pprint import pprint
import requests
import json

API_KEY = '069afb29-fba1-49fd-8c18-2ba9fee4ed91'

def get_address(lat, lon):

    URL = f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={lat},{lon}&format=json&sco=latlong&kind=house&results=1&lang=ru_RU"
    result = requests.get(URL).json()
    return result['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']

lat = '55.608912'
lon = '37.984516'
e = get_address(lat, lon)

print(f'Адресом обьекта с долготой {lon} и широтой {lat} является: {e} \n')

r = requests.get(f"https://geocode-maps.yandex.ru/1.x/?apikey={API_KEY}&geocode={lat},{lon}&format=json&sco=latlong&kind=house&results=1&lang=ru_RU")
j_data = r.json()
print('Сохраняемый в файл yandex_map.json :\n')
pprint(j_data)
with open('yandex_map.json', 'w') as f:
    json.dump(r.json(), f)