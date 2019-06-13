@echo off
Rem This deploys to Kento's Jetson Nano, you need the kento_id private key pair
ssh kento@10.0.0.112
cd Documents/audiocleanup
python train.py
