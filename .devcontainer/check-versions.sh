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
if [ -f "/root/.config/opencode/get-shit-done/VERSION" ]; then
    cat "/root/.config/opencode/get-shit-done/VERSION"
elif [ -f "$HOME/.config/opencode/get-shit-done/VERSION" ]; then
    cat "$HOME/.config/opencode/get-shit-done/VERSION"
else
    echo "GSD not found in OpenCode config directory"
    exit 1
fi

echo ""
echo "Pyright:"
pyright --version

echo ""
echo "Specify:"
specify --version || specify --help > /dev/null && echo "Specify CLI is installed (version check unavailable)"

echo ""
echo "All tools verified successfully!"
