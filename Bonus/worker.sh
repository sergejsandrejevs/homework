#!/bin/bash

if [ !-e $1 ]
   then
       echo "Please, specify name of the machine you want to create"
       exit 0
   else
       sed -i '/\Wworker/s/worker[0-9]*/'$1'/g' Vagrantfile
       sed -i '/\Wworker/s/worker[0-9]*/'$1'/g' playbook_worker.yml
       vagrant up
fi
