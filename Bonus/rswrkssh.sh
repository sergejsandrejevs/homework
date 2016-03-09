#!/bin/bash

#This script allows you to establish ssh connection to worker machines

if [ !-e $1 ]
   then
       echo "Please, specify name of the machine you want to connect to"
       exit 0
else
    sed -i '/\Wworker/s/worker[0-9]*/'$1'/g' Vagrantfile
    vagrant ssh $1
fi
