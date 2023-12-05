#!/usr/bin/env python3

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

src = """./scripts/genservconf.py
./scripts/gencliconf.py
scp ./serv-conf/""" + iniConf['server-interface'] + '.conf ' + \
iniConf['ssh-target'] + ':./' + '\n' + \
'ssh -t ' + iniConf['ssh-target'] + ' \'sudo wg-quick down ' + iniConf['server-interface'] + '\'' + '\n' \
'ssh -t ' + iniConf['ssh-target'] + ' \'sudo mv ' + iniConf['server-interface'] + '.conf /etc/wireguard/\'' + '\n' \
'ssh -t ' + iniConf['ssh-target'] + ' \'sudo wg-quick up ' + iniConf['server-interface'] + '\'' + '\n'

print(src)
