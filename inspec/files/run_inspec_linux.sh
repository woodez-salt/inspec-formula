#!/bin/bash

export HOME="/root" 
cd /var/tmp/inspec-test
inspec exec . --reporter=json:/var/tmp/test.json
