#!/bin/bash

#Connect to the mater of the staging wazuh account

KUBE_EDITOR="nano" kubectl edit pod wazuh-indexer-0 -n wazuh
