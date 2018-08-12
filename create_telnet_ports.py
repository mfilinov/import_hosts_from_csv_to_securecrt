# -*- coding: utf-8 -*-
import argparse
import csv
parser = argparse.ArgumentParser(description='generate ports')
parser.add_argument('-start', action="store", dest="start", type=int)
parser.add_argument('-stop', action="store", dest="stop", type=int)
parser.add_argument('-ip', action="store", dest="ip", type=str, default='127.0.0.1')
parser.add_argument('-f', action="store", dest="folder", type=str, default='')
args = parser.parse_args()
header = ['session_name', 'hostname', 'folder', 'protocol', 'port', 'emulation']
def generate_telnet_ports(start,stop,folder,ip):
    result = []
    for i in range(start, stop + 1):
        list_result = ['port_' + str(i), ip, folder, 'telnet', i, 'xterm']
        result.append(list_result)
    return result
telnet_list = generate_telnet_ports(start=args.start,stop=args.stop,folder=args.folder,ip=args.ip)
'''write header'''
with open('to_securecrt.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(header)
'''append sessions'''
with open('to_securecrt.csv', 'a') as f:
    writer = csv.writer(f, delimiter=',')
    for row in telnet_list:
        writer.writerow(row)