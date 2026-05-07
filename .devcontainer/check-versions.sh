#!/bin/bash
set -euo pipefail

echo "Checking installed tool versions..."
echo ""

echo "OpenCode:"
opencode --version

echo ""
echo "Ralphy:"
ralphy --version

echo ""
echo "uv:"
uv --version

echo ""
echo "Pyright:"
pyright --version

echo ""
echo "Python:"
python3 --version

echo ""
echo "Node.js:"
node --version

echo ""
echo "All workshop tools verified successfully!"
