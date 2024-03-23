#!/bin/bash

scripts/gendeploy.py > tmp.sh && \
bash tmp.sh
rm tmp.sh

