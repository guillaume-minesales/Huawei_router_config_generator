#!/usr/bin/env python3

import shutil

print('******************************\n')
print('Huawei Router Config Generator\n')
print('******************************\n')
print('Case 1 : CPE with Firewall/Router interconnection\n')
print('Case 2 : CPE with LAN management\n')
case = input('Which case to use ?(1-2) \n')

if case == '1':
    # Copying template
    shutil.copyfile('template1.txt', 'config.txt')
    # Hostname
    print('*** Step 1 ***')
    hostname = input('Hostname : ')
    # LAN Vlan
    print('*** Step 2 ***')
    vlan_choosed = input('LAN Vlan to use : ')
    # Network Config + Interco
    print('*** Step  3 ***')
    ip_interco = input('CPE IPv4 address (without mask) : ')
    ip_interco_mask = input('CPE IPv4 address mask : ')
    ip_interco_pe = input('PE IPv4 address (without mask) : ')
    ip_cpe_interco = input('CPE IPv4 address for router/firewall interconnection :')
    ip_cpe_interco_mask  = input('CPE IPv4 address mask for router/firewall interconnection :')
    # Opening files
    template = open('template1.txt', 'r')
    config = open('config.txt', 'w')
    # Populating wordlists
    checkWords = ('sysname generic','vlan batch 10', 'vlan 10', '192.0.0.0', '255.0.0.0', '192.0.0.1', '185.0.0.0', '255.255.0.0')
    repWords = ('sysname ' + hostname, 'vlan batch ' + vlan_choosed, 'vlan ' + vlan_choosed, ip_interco, ip_interco_mask, ip_interco_pe, ip_cpe_interco, ip_cpe_interco_mask)
    # Replacing words
    for line in template:
        for check, rep in zip(checkWords, repWords):
            line = line.replace(check, rep)
        config.write(line)
    config.close()
    template.close()

else:
    print('Coming soon')
