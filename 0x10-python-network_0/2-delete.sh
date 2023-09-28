#!/bin/bash
# This script sends a DELETE request to the URL provided as the first argument and displays the body of the response.
curl -s -X DELETE "$1"
