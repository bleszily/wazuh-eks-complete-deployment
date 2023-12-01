#!/bin/bash

#Connect to the mater of the staging wazuh account

kubectl -n wazuh describe pod wazuh-dashboard-7c4c58d45-t4nfl
