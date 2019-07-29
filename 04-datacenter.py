#!/usr/bin/python3 

import json

def main():
    with open('data/datacenter.json') as datacenter:
        datacenter_string = datacenter.read()

    print(datacenter_string)
    print(type(datacenter_string))

    datacenter_decoded = json.loads(datacenter_string)
    print(datacenter_decoded)
    print(type(datacenter_decoded))

    print(datacenter_decoded['row3'])
    print(datacenter_decoded['row2'][0])

main()
