#!/data/data/com.termux/files/usr/bin/bash

pkg update -y
pkg upgrade -y

pkg install python git clang libjpeg-turbo -y

pip install -r requirements.txt

echo
echo "Installation Complete."
echo
echo "Run:"
echo "python main.py"
