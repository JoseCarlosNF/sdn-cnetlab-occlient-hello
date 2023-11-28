# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", disabled: false
  config.vm.box = "ubuntu/focal64"
  config.vm.box_check_update = false

  config.vm.define "cnetlab" do |host|
    host.vm.hostname = "cnetlab"
    host.vm.network "private_network", ip: "192.168.56.20"
    host.vm.provider "virtualbox" do |vb|
      vb.name = "cnetlab"
      vb.memory = "1024"
      vb.cpus = 2
    end
  end

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y tmux git python3-pip xterm
    curl -fSsl https://get.docker.com | sh
    git clone https://git.rnp.br/cnar/sdn-multicamada/emulacao/emulador-optico.git
    git clone https://github.com/lbors/sdnm-clab.git
    cd emulador-optico
    pip install pyYAML
    pip install -r requirements.txt
    python3 setup.py install
  SHELL
end
