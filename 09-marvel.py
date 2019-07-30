#!/usr/bin/python3

import uuid
import argparse
import time
import hashlib
from pprint import pprint

import requests

API_ENDPOINT = 'https://gateway.marvel.com:443/v1/public/characters?name=Wolverine'

def create_key(pub=None, priv=None, ts=None):
    return hashlib.md5((ts+priv+pub).encode('utf-8')).hexdigest()

def read_key(key_location):
    with open(key_location, 'r') as kf:
        return kf.read().rstrip('\n')

def main(args):
    current_time = str(time.time()).rstrip('.')
    priv_key = read_key(args.priv)
    pub_key = read_key(args.pub)

    key_hash = create_key(pub=pub_key, priv=priv_key, ts=current_time)
    req_site = f'{API_ENDPOINT}&ts={current_time}&apikey={pub_key}&hash={key_hash}'
    info = requests.get(req_site).json()

    print(f'ID: {info["data"]["results"][0]["id"]}')
    print(f'Name: {info["data"]["results"][0]["name"]}')
    print(f'Description: {info["data"]["results"][0]["description"]}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pub', type=str, help='Priv key location')
    parser.add_argument('--priv', type=str, help='Pub key location')
    args = parser.parse_args();
    main(args)
    
