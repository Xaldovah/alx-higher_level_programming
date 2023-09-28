#!/bin/bash
# This script sends a JSON POST request to the URL provided as the first argument, with the contents of the file specified as the second argument, and displays the body of the response.
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
