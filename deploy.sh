#!/usr/bin/env bash

cd $(dirname $0)
ansible-galaxy install williamyeh.prometheus
ansible-galaxy install ansiblebit.grafana
ansible-playbook -b "$@" site.yml
