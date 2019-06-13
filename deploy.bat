@echo off
Rem This deploys to Kento's Jetson Nano
curl -d '{"build":1}' -H "Content-Type: application/json" -X POST http://teamsudocode.herokuapp.com/post