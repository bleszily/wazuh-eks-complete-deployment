#!/bin/bash

#Start the  sso login session

aws sso login --profile '698****_AWS-rw-All'

sleep 10

export AWS_DEFAULT_PROFILE='698***_AWS-rw-All'

aws sts get-caller-identity
