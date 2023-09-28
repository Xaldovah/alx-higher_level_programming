#!/bin/bash
# This script makes a request to the specified URL, causing the server to respond with "You got me!"
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: HolbertonSchool" -d "user_id=98"
