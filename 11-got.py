#!./usr/bin/python3
import requests
from pprint import pprint

API_SRC = '''https://www.anapioficeandfire.com/api/houses'''

def get_got():
    current_page = 1
    houses = []

    while True:
        params = {
                'pagesize': 50,
                'page': current_page
            }
        try:
            data = requests.get(API_SRC, params)
        except Exception as e:
            print(f'Error querying API - {e}')
            return None
        else:
            #print('API queried successfully')

            if len(data.json()) == 0: break
            houses.extend(data.json())

            current_page += 1

    print(f'Number of houses: {len(houses)}')
    print(f'House example:')
    ret = ''
    for i in range(10):
        ret += f'<br>{houses[i+13]["name"]} - {houses[i+13]["region"]}'
        #print(f'\t{houses[i+13]["name"]} - Location {houses[i+13]["region"]}')
        #print(f'\tOverlord: {houses[i+13]["overlord"]}')

    return ret

if __name__ == '__main__':
    get_got()
