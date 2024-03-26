# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.ssh.extra_args = ["-t", "sudo", "-i", "tmux"]

  config.vm.synced_folder ".", "/vagrant", disabled: false
  config.vm.box = "ubuntu/focal64"
  config.vm.box_check_update = false

  config.vm.define "cnetlab" do |host|
    host.vm.hostname = "cnetlab"
    host.vm.network "private_network", ip: "192.168.56.20"
    host.vm.provider "virtualbox" do |vb|
      vb.name = "cnetlab"
      vb.memory = "4096"
      vb.cpus = 2
    end
  end

  config.vm.provision "shell", inline: <<-SHELL
#!/usr/bin/env bash
echo '------------------------------- Set workdir ----------------------------------'
    cd /root
    cp /home/vagrant/.ssh/authorized_keys /root/.ssh/authorized_keys

echo '-------------------------- Install basic packages ----------------------------'
    apt-get update
    apt-get install -y fish tmux git python3-pip xterm
    chsh -s $(which fish) vagrant
    chsh -s $(which fish) root

echo '------------------------------- Install adsf ---------------------------------'
    git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.13.0

    # fish
    # HACK: fish has conflict to completions in fish installed version. Therefore the reference to /etc/
    grep -qF 'source $HOME/.asdf/asdf.fish' /etc/fish/config.fish || echo 'source $HOME/.asdf/asdf.fish' >> /etc/fish/config.fish
    mkdir -p ~/.config/fish/completions
    ln -s ~/.asdf/completions/asdf.fish ~/.config/fish/completions

    # bash
    grep -qF '. "$HOME/.asdf/asdf.sh"' /root/.bashrc               || echo '. "$HOME/.asdf/asdf.sh"' >> /root/.bashrc
    grep -qF '. "$HOME/.asdf/completions/asdf.bash"' /root/.bashrc || echo '. "$HOME/.asdf/completions/asdf.bash"' >> /root/.bashrc

    /root/.asdf/bin/asdf plugin-add fx
    /root/.asdf/bin/asdf install fx 33.0.0
    /root/.asdf/bin/asdf global fx 33.0.0

    /root/.asdf/bin/asdf plugin-add jq
    /root/.asdf/bin/asdf install jq 1.7.1
    /root/.asdf/bin/asdf global jq 1.7.1

    /root/.asdf/bin/asdf plugin-add golang
    /root/.asdf/bin/asdf install golang 1.21.0
    /root/.asdf/bin/asdf global golang 1.21.0

echo '------------------------------ Install docker --------------------------------'
    apt list --installed | grep docker || curl -fSsl https://get.docker.com | sh

echo '------------------------------- Install cnetlab -------------------------------'
    test -d sdnm-clab       || git clone https://github.com/lbors/sdnm-clab.git
    test -d emulador-optico || git clone https://git.rnp.br/cnar/sdn-multicamada/emulacao/emulador-optico.git
    cd emulador-optico
    pip install pyYAML
    pip install -r requirements.txt

echo '------------------------------- Install cnetlab -------------------------------'
    python3 setup.py install
  SHELL
end
