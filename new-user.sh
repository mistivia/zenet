#!/bin/bash

wg genkey > tmpsk
cat tmpsk | wg pubkey > tmppk
echo "$1 $(cat tmppk) $(cat tmpsk)" >> profiles
rm tmpsk
rm tmppk
