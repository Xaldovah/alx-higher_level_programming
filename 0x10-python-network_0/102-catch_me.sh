#!/bin/bash
# This script makes a request to the specified URL, causing the server to respond with "You got me!"
curl -s http://0.0.0.0:5000/catch_me | grep "You got me!"
