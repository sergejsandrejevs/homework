# -*- mode: ruby -*-
# vi: set ft=ruby :

WORKERS = 2
ANSIBLE_GROUPS = {
  "centrals" => ["central"],
  "workers" => ["worker[1:#{WORKERS}]"]
}
#10.10.0.2
#10.10.0.11
#10.10.0.12
#...

Vagrant.configure(2) do |config|
  config.vm.define "central" do |central_config|
    central_config.vm.hostname = "central"
    central_config.vm.box = "centos6"
    central_config.vm.box_url = "https://atlas.hashicorp.com/vdribadan/boxes/centos6/versions/1.0/providers/virtualbox.box"
    central_config.vm.network "private_network", :ip => "10.10.0.2"
    central_config.vm.provider "virtualbox" do |v|
      v.memory = 1024
      v.cpus = 1
    end
    central_config.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "playbook_central.yml"
      ansible.verbose = true
      ansible.host_vars = {
        "central" => {
          "ip_address" => "10.10.0.2",
          "dns_name" => "central"   
        }
      }
    end
  end

  (1..WORKERS).each do |worker_id|
    config.vm.define "worker#{worker_id}" do |worker_config|
      worker_config.vm.hostname = "worker#{worker_id}"
      worker_config.vm.box = "centos6"
      worker_config.vm.box_url = "https://atlas.hashicorp.com/vdribadan/boxes/centos6/versions/1.0/providers/virtualbox.box"
      worker_config.vm.network "private_network", :ip => "10.10.0.#{10+worker_id}"
      worker_config.vm.provider "virtualbox" do |v|
        v.memory = 512
        v.cpus = 1
      end
      worker_config.vm.provision "ansible_local" do |ansible|
        ansible.playbook = "playbook_worker.yml"
        ansible.verbose = true
        ansible.host_vars = {
          "worker#{worker_id}" => {
            "zabbix_server_ip_address" => "10.10.0.2",
            "ip_address" => "10.10.0.#{10+worker_id}",
            "dns_name" => "worker#{worker_id}"   
          }
        }
      end
    end
  end
end
