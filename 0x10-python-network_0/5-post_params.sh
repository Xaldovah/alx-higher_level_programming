#!/bin/bash
# This script sends a POST request to the URL provided as the first argument, including variables email and subject with specified values, and displays the body of the response.
curl -s -X POST "$1" -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
