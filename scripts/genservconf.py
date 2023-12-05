#!/usr/bin/env python3

import os

os.system("mkdir -p ./serv-conf/")

def readIniConf():
    conf = dict()
    with open('config.ini') as fp:
        for line in fp:
            if len(line.strip()) == 0: continue
            s = line.split('=', 1)
            key = s[0].strip()
            value = s[1].strip()
            conf[key] = value
    return conf

iniConf = readIniConf()

server = iniConf['server']
port = iniConf['server-port']
sshTarget = iniConf['ssh-target']
serverPk = iniConf['server-pubkey']
serverSk = iniConf['server-privkey']
network = iniConf['network-prefix']
interface = iniConf['server-interface']




def parseProfiles():
    names = list()
    pks = list()
    sks = list()
    with open("profiles") as fp:
        for line in fp:
            fields = line.strip().split(" ")
            names.append(fields[0])
            pks.append(fields[1])
            sks.append(fields[2])
    return names, pks, sks

names, pks, sks = parseProfiles()

config = '[Interface]\n' + \
    'Address = ' + network + '1/24' + '\n' + \
    'SaveConfig = true\n' + \
    'ListenPort = ' + port + '\n' + \
    'PrivateKey = ' + serverSk + '\n\n'

for i in range(len(names)):
    config = config + '#' + names[i] + '\n'
    config = config + '[Peer]' + '\n'
    config = config + 'PublicKey = ' + pks[i] + '\n'
    config = config + 'AllowedIPs = ' + network + str(i+10) + '\n\n' 

with open('serv-conf/' + interface + '.conf', "w") as fp:
    fp.write(config)

hosts = ""
for i in range(len(names)):
    hosts = hosts + network + str(i+10) + ' ' + names[i] + '\n'
with open("hosts", "w") as fp:
    fp.write(hosts)

