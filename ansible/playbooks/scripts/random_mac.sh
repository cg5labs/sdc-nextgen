#!/usr/bin/env bash

if [[ ! -d scripts/venv ]]; then
  python3 -m venv scripts/venv
  source venv/bin/activate
  pip3 install -r scripts/requirements.txt
else
  source scripts/venv/bin/activate
fi

python3 scripts/random_mac.py

