#!/bin/bash

#Connect to the mater of the staging wazuh account

KUBE_EDITOR="nano" kubectl edit pod wazuh-dashboard-7c4c58d45-t4nfl -n wazuh
