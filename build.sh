#!/bin/bash

curl https://sh.rustup.rs -sSf | sh -s -- -y
source $HOME/.cargo/env
rustup default stable

# Upgrade pip
pip install --upgrade pip

# Install all requirements including gunicorn
pip install -r requirements.txt

# Just to check gunicorn installed
gunicorn --version
