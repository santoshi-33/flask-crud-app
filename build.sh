#!/bin/bash

# Install Rust toolchain silently
curl https://sh.rustup.rs -sSf | sh -s -- -y

# Load Rust environment variables so rust commands work
source $HOME/.cargo/env

# Set Rust to use the stable version by default
rustup default stable

# Install Python dependencies from requirements.txt
pip install -r requirements.txt
