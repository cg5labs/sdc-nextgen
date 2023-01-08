#!/usr/bin/env bash

if [[ ! -d scripts/venv ]]; then 
  python3 -m venv scripts/venv
  pip3 install -r scripts/requirements.txt
  source scripts/venv/bin/activate
else
  source scripts/venv/bin/activate
fi

python3 scripts/random_host.py

