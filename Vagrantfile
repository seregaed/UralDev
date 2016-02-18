# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "trusty64"
  config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box"

  config.vm.network "forwarded_port", guest: 8080, host: 8084

  config.vm.synced_folder ".", "/home/vagrant/src"

  config.vm.provider :virtualbox do |vb|
    vb.cpus = 1
    vb.memory = 190
  end

  config.vm.provision "shell" do |s|
    s.inline = "/home/vagrant/src/deploy/vagrant/prepare.sh"
    s.binary = true
  end

  config.vm.provision "shell" do |s|
    s.inline = "/home/vagrant/src/deploy/vagrant/venv.sh"
    s.privileged = false
    s.binary = true
  end

  # config.vm.provision "shell" do |s|
  #   s.inline = "/home/vagrant/src/deploy/vagrant/static.sh"
  #   s.privileged = true
  #   s.binary = true
  # end

end
