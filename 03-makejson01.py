#!/usr/bin/python3
import json

def main():
    hitchhikers = [{'name': 'Zaphoid Beebelbrocks', 'species': 'Beetlejuciaan'},
            {'name': 'Arthur Dent', 'species': 'Human'}]

    with open('data/galaxy_guide.json', 'w') as dfile:
        json.dump(hitchhikers, dfile)

if __name__ == '__main__':
    main()
