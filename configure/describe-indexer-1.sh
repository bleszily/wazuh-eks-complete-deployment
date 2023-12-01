#!/bin/bash

#Connect to the mater of the staging wazuh account

kubectl -n wazuh describe pod wazuh-indexer-1
