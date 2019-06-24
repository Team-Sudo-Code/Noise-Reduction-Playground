@echo off
Rem This deploys to Kento's Jetson Nano, you need the kento_id private key pair
curl -d "build=1" -X POST http://teamsudocode.herokuapp.com/mlbackend
