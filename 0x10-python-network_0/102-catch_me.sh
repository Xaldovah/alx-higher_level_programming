#!/bin/bash
# This script makes a request to the specified URL, causing the server to respond with "You got me!"
curl -s -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "$1"
