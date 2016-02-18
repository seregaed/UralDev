#!/bin/bash

set -e

echo "Setup hostname"
hostname vagrant-ural

echo "Some terminal fix"
export LC_ALL="C"
export DEBIAN_FRONTEND='noninteractive apt-get -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" dist-upgrade'

echo "Cleanup"
apt-get remove -y chef puppet
apt-get autoremove -y

echo "Add python repository"
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv DB82666C
echo 'deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu trusty main' > /etc/apt/sources.list.d/fkrull-deadsnakes-trusty.list

echo "Update and install apt packages"
apt-get update
# apt-get -y upgrade
apt-get -y install \
    language-pack-ru-base \
    curl git htop iftop mercurial pydf vim zip zsh \
    python3.5 python3.5-dev python3.5-venv

echo "Update locale"
# export LC_ALL=`locale --all | grep -i ru_RU.utf`
update-locale "LC_ALL=`locale --all | grep -i ru_RU.utf`"
