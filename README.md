As base for majority goals there was reused existing solution (see forked from Maksim Koskin# homework).
Vagrant version: 1.9.8

Goals summary:
1. yes
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
	Inside Vagrantfile:
		Two virtual machines types - central and worker. Zabbix server is installed on central, both hosts are configured for monitoring with zabbix agents installed. 
			Zabbix server url: http://10.10.0.2/zabbix 
				Login: admin Password: zabbix
		Rabbitmq Server is up and running on central machine.
			Rabbitmq management url: http://10.10.0.2:15672/
			Login: guest 
			Password: guest
		Worker nodes are scalable (change number in Vagrantfile) from 0 to N.
		
		
	Tests:	
		Run python /vagrant/consumer.py on worker machine to start receiving messages. Consumer accepts messages and sleeps for received amount of seconds.
		Java installation and producer.java built wasn't automated yet, but the bash steps can be found at build_instructions.txt file. An example shows how to send a message to sleep for 2s seconds:
			cd /vagrant/
			export CP=.:amqp-client-4.0.2.jar:slf4j-api-1.7.21.jar:slf4j-simple-1.7.22.jar
			javac -cp $CP Producer.java
			java -cp $CP Producer 2
		Run /vagrant/turtle.sh to produce queue of unacknowledged messages.
			
			
	Zabbix:
            Run turtle.sh several times in order to see trigger, mentioned in specification.