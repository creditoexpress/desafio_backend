#!/bin/bash

docker-compose down &&
docker rmi -f backend-test_api:latest &&
docker-compose up -d --build