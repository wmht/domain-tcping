#! /bin/bash

docker build -t reg.nexus.wmq.com/tools/domain-ping:v1 .
docker push reg.nexus.wmq.com/tools/domain-ping:v1