#!./usr/bin/python3
import requests
from pprint import pprint

API_SRC = '''https://www.anapioficeandfire.com/api/houses'''

def get_got(specific_house = None):
    current_page = 1
    houses = []

    print('Querying API')
    while True:
        print('Page: ' + str(current_page))
        params = {
                'pagesize': 50,
                'page': current_page
            }
        try:
            data = requests.get(API_SRC, params)
        except Exception as e:
            print(f'Error querying API - {e}')
            return None

        if len(data.json()) == 0: break
        houses.extend(data.json())

        current_page += 1

    ret = ''

    print('Formatting data')
    if specific_house is None:
        for i in range(len(houses)):
            if houses[i]["region"] is None:
                ret += f'<br>{houses[i]["name"]} - WHO KNOWS'
            else:
                ret += f'<br>{houses[i]["name"]} - {houses[i]["region"]}'
    else:
        for house in houses:
            if house["name"] == specific_house:
                ret += '<hr>'
                ret += f'<h3><u>{house["name"]} - {house["region"]}</u></h3>'
                ret += f'<p>Words: {house["words"]}</p>'
                ret += f'<p>Coat of Arms: {house["coatOfArms"]}</p>'
                ret += f'<p>Ancestral Weapons: {house["ancestralWeapons"]}</p>'
                if "seats" in house:
                    ret += 'Seats <ol>'
                    for seat in house["seats"]:
                        ret += f'<li>{seat}</li>'
                    ret += '</ol>'
                if "titles" in house:
                    ret += 'Titles <ol>'
                    for title in house["titles"]:
                        ret += f'<li>{title}</li>'
                    ret += '</ol>'

        if ret is '':
            ret = f'{specific_house} not found'
    return ret

if __name__ == '__main__':
    get_got()
