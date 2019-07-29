#!/usr/bin/python3

import yaml

def main():
    vcp =  [{'service': 'compute', 'app': 'nova'},
            {'service': 'network', 'app': 'neutron'},
            {'service': 'block', 'app': 'cinder'}]

    print(vcp)

    with open('data/vcp.yaml', 'w') as vcp_file:
        yaml.dump(vcp, vcp_file)

if __name__ == '__main__':
    main()
