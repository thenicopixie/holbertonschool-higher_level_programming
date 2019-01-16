#!/bin/bash
# This script sends a JSON POST request to a URL.
# Displays the body of the response
curl -s -H "Content-Type: application/json" -X POST -d @$2 $1
