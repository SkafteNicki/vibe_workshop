#!/bin/bash
set -e

echo "Checking installed tool versions..."
echo ""

echo "OpenCode:"
opencode --version

echo ""
echo "Ralphy:"
ralphy --version

echo ""
echo "Get Shit Done CC:"
get-shit-done-cc --version

echo ""
echo "Pyright:"
pyright --version

echo ""
echo "Specify:"
specify --version || specify --help > /dev/null && echo "Specify CLI is installed (version check unavailable)"

echo ""
echo "All tools verified successfully!"
