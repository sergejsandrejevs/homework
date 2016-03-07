#!/bin/bash


sed -i '/\Wworker/s/worker[0-9]*/'$1'/g' Vagrantfile
sed -i '/\Wworker/s/worker[0-9]*/'$1'/g' playbook_worker.yml

vagrant up
