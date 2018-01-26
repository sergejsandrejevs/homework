As base for majority goals there was reused existing solution (see forked)

Goals summary:
1. yes (vagrant 1.8 was used)
2. yes
3. yes (classpath and libs still to be downloaded manually yet)
4. yes
5. CPU - yes
   RAM - yes
   HDD - no
6. yes (wasn't checked)
7. yes
8. yes

Centos6.box is a Centos6.7 basic installation with Ansible 2.0.1.0 preinstalled.
Because of the bug in Vagrant 1.8.1 (promised to be fixed in 1.8.2) when using ansible 2.0. as ansible_local provisioner you need to make changes in Vagrant configuration on your host machine as follows:
Windows machine:
Modify C:\HashiCorp\Vagrant\embedded\gems\gems\vagrant-1.8.1\plugins\provisioners\ansible\provisioner\guest.rb file as described in here: https://github.com/mitchellh/vagrant/commit/9dbdb9397a92d4fc489e9afcb022621df7f60d11
As an option you can just replace guest.rb on your machine with file provided in archive.
That's it - you can now cd to Homework dir and run vagrant up.

			
    Archive Contents:
	    Configuration files, scripts for running rabbitmq queue etc.

	
	
	Inside Vagrantfile:
		Two virtual machines - central and worker. Zabbix server is installed on central, both hosts are configured for monitoring with zabbix agents installed. 
			Zabbix server url: http://10.10.10.3/zabbix 
				Login: admin Password: zabbix
		Rabbitmq Server is up and running on central machine.
			Rabbitmq management url: http://10.10.10.3:15672/
			Login: guest 
			Password: guest
		
		
		
	Tests:	
		Run python /vagrant/consumer.py on worker machine to start receiving messages. Consumer accepts messages  and sleeps for received amount of seconds.
		Java installation and producer.java built wasn't automated yet, but the bash steps can be found at build_instructions.txt file. An example shows how to send a message to sleep for 2s seconds:
			cd /vagrant/
			export CP=.:amqp-client-4.0.2.jar:slf4j-api-1.7.21.jar:slf4j-simple-1.7.22.jar
			javac -cp $CP Producer.java
			java -cp $CP Producer 2
		Run /vagrant/turtle.sh to produce queue of unacknowledged messages.
			
			
	Zabbix:
                Run turtle.sh several times in order to see trigger, mentioned in specification.


        Bonus task: 
                    You can now cd to Homework/Bonus and run ./worker.sh worker#(any number eg. ./worker.sh worker5).
                    New host will be added and registered in zabbix monitoring system, so one can run python /vagrant/consumer.py on this host and start receiving messages
		    Use rswrkssh.sh (Example usage: ./rswrkssh.sh worker3) to ssh to vagrant machine "lost" due to Vagrantfile change.


        Known issues:
	             Zabbix monitoring may not fetch all itmes from machines, created by worker.sh script since they are located in different subnet. Probably due to my home router problems.
		
		
		
		
		
		
		
		
		
		
		
(c) Maksim Koskin# homework
