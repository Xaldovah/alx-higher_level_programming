#!/bin/bash
# Takes a URL as an argument, sends a GET request to that URL using curl, and displays the body of the response for a 200 status code.
curl -s -o /tmp/body "$1" && cat /tmp/body
