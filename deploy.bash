#!/bin/bash
# curl -d '{"build":1}' -H "Content-Type: application/json" -X POST http://teamsudocode.herokuapp.com/mlbackend
curl -d "build=1" -X POST http://127.0.0.1:8000/mlbackend