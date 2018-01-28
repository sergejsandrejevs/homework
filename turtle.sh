#!/bin/bash

#This is a rabbitmq overload script

for i in {1..1000}
do
  python /vagrant/producer.py '1';
done
