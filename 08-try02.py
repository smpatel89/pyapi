#!/usr/bin/python3

import sys

def main():
    while True:
        try:
            print('Divide x by y')
            x = int(input('\tx: '))
            y = int(input('\ty: '))
            print(f'Result: x/y = {x/y}')
        except ZeroDivisionError as zerr:
            print(f'y cannot be 0\n{zerr}')
        except Exception as e:
            print('------------------')
            print(f'Unknown error {e}')
            print('------------------')
            print(f'{sys.exc_info()[0]}')
            print('------------------')
            raise

if __name__ == '__main__':
    main()
