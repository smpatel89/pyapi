#!/usr/bin/python3

def main():
    lst = ['cisco', 'juniper', 'bigip', 'tellabs', 'meraki']
    print(f'Third vendor: {lst[2]}')

    lst.append('nortel')
    print(f'Last vendor: {lst[-1]}')

if __name__ == '__main__':
    main()
