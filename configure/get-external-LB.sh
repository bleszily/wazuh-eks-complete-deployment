#!/bin/bash

#Get the external LB DNS for browser connection

kubectl -n wazuh get services -o wide
