#!/usr/bin/python3

def main():
    host_ip_dict = {'host01': '10.0.0.2', 'host02': '192.168.70.1', 
            'host03': '8.8.8.8'}
    print(f'Host2 - {host_ip_dict["host02"]}')

    host_ip_dict['host04'] = '172.0.0.1'
    host_ip_dict.update({'host05': '9.9.9.9'})
    print(f'Host4 - {host_ip_dict["host04"]}')
    print(f'Host5 - {host_ip_dict["host05"]}')

    print(host_ip_dict.get('host66'))
    

if __name__ == '__main__':
    main()
