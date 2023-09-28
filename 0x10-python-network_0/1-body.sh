#!/bin/bash
# Takes a URL as an argument, sends a GET request to that URL using curl, and displays the body of the response for a 200 status code.
curl -sL "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi
