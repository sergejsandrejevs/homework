#!/bin/bash

#This is a rabbitmq overload script

for run in {1..20}
do
  python /vagrant/producer.py 'Move on, you damned turtle!'
done
