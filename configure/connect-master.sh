#!/bin/bash

#Connect to the mater of the staging wazuh account

kubectl exec -it wazuh-manager-master-0 -n wazuh -- bin/bash
