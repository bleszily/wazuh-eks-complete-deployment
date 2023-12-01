#!/bin/bash

#Connect to the mater of the staging wazuh account

KUBE_EDITOR="nano" kubectl edit pod wazuh-logstash-0 -n wazuh
