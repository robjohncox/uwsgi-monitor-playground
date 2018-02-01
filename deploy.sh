#!/usr/bin/env bash

cd $(dirname $0)
ansible-playbook -b site.yml
