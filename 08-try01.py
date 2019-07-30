#!/usr/bin/python3


def main():
    name = input('Enter a file name: ')
    with open(f'data/{name}', 'w') as input_file:
        input_file.write('Well done')

while True:
    try:
        main()
    except IsADirectoryError:
        print(f'Put in a file name')
    else:
        print('File created successfuly')
        break
