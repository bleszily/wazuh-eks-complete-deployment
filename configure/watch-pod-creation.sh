#!/bin/bash

#Watch the creation of Pods

watch -n 1 'kubectl -n wazuh get pods'
