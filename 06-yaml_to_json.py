#!/usr/bin/python3

import json
import yaml

def main():
    with open('data/vcp.yaml', 'r') as input_file:
        data = yaml.load(input_file)

    print(data)

    with open('data/vcp.json', 'w') as output_file:
        json.dump(data, output_file)

if __name__ == '__main__':
    main()
