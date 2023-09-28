#!/bin/bash
# Sends a GET request to the URL provided as the first argument, including a custom header X-School-User-Id with the value 98, and displays the body of the response.
curl -s -H "X-School-User-Id: 98" "$1"
