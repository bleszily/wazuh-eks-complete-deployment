#!/bin/bash

#Connect to the mater of the staging wazuh account

kubectl exec -it wazuh-dashboard-7c4c58d45-t4nfl -n wazuh -- /bin/bash
