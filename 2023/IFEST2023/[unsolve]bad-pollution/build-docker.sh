#!/bin/bash
docker rm -f bad_pollution
docker build -t bad_pollution . 
docker run --name=bad_pollution --rm -p55213:55213 -it bad_pollution
