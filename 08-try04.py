#!/usr/bin/python3
import uuid

ticket = uuid.uuid1()

try:
    print('Please type the config file to load')
    config_file = input('filename: ')
    config_file_obj = open('data/'+config_file, 'r')
    switch_config = config_file_obj.read()
except:
    x = 'Error with obtaining config file info'
else:
    x = 'Switch file found'
finally:
    close(config_file_obj)
    with open('data/try04.log', 'a') as zlog:
        print('\n\nWriting results to log')
        print(ticket, ' - ', x, file=zlog)
    
