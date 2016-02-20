#!/bin/bash 

set -e #exit if error

echo "cd src" >> /home/vagrant/.bashrc #print directory
echo "cd src" >> /home/vagrant/.zprofile


echo "Create python virtual environment"
pyvenv-3.5 "/home/vagrant/env"  #create virtual environment with python 3.5
source "/home/vagrant/env/bin/activate" #start second script in this 
pip install -U pip  #install (upgrade?) pip
echo 'source "/home/vagrant/env/bin/activate"' >> /home/vagrant/.bashrc
echo 'source "/home/vagrant/env/bin/activate"' >> /home/vagrant/.zprofile

echo "Install python packages"
cd "/home/vagrant/src" #change direcrtory
pip install -e . #start second script in this directrory, install pip-packages 
