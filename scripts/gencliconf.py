#!/usr/bin/env python3

import os

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

def cliConf(sk, i):
    config = "[Interface]\n"
    config = config + 'PrivateKey = ' + sk + '\n'
    config = config + 'Address = ' + network + str(i+10) + '/32\n\n'
    config = config + '[Peer]\n' + \
        'PublicKey = ' + serverPk + '\n' + \
        'AllowedIPs = ' + network + '0/24' + '\n' + \
        'Endpoint = ' + server + ':' + port + '\n' + \
        'PersistentKeepalive = 20\n'
    return config


names, pks, sks = parseProfiles()

for i in range(len(names)):
    os.system("mkdir -p " + './cli-confs/' + names[i])
    with open("./cli-confs/" + names[i] + '/wg123.conf', "w") as fp:
        fp.write(cliConf(sks[i], i))

