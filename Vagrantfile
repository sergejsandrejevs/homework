# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.define "central" do |central_config|
    central_config.vm.hostname = "central"
    central_config.vm.box = "centos6"
    central_config.vm.box_url = "https://atlas.hashicorp.com/vdribadan/boxes/centos6/versions/1.0/providers/virtualbox.box"
    central_config.vm.network "private_network", :ip => '10.10.10.3'
    central_config.vm.network "forwarded_port", guest: 22, host: 5343, id: "ssh"
    central_config.vm.network "forwarded_port", guest: 80, host: 2341
    central_config.vm.network "forwarded_port", guest: 443, host: 4531
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook_central.yml"
    ansible.verbose = true
  end
  end

  config.vm.define "worker" do |worker_config|
    worker_config.vm.hostname = "worker"
    worker_config.vm.box = "centos6"
    worker_config.vm.box_url = "https://atlas.hashicorp.com/vdribadan/boxes/centos6/versions/1.0/providers/virtualbox.box"
    worker_config.vm.network "private_network", :ip => '10.10.10.2'
    worker_config.vm.network "forwarded_port", guest: 22, host: 7433, id: "ssh"
    worker_config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.provision "ansible_local" do |ansible|
    ansible.playbook = "playbook_worker.yml"
    ansible.verbose = true
  end
  end 
end
