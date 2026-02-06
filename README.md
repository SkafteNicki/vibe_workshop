# OpenCode Dev Container

A minimal development container with OpenCode pre-installed.

## Quick Start

1. Open this repository in VS Code
2. When prompted, click "Reopen in Container" (or run the command "Dev Containers: Reopen in Container")
3. Wait for the container to build and start
4. Open the integrated terminal and run:
   ```bash
   opencode
   ```

## First Time Setup

This workspace is pre-configured to use the **Kimi K2.5 Free** model from Moonshot AI. After starting OpenCode for the first time:

1. Run the `/connect` command in OpenCode
2. Search for and select **Moonshot AI**
3. Get your free API key from [platform.moonshot.ai](https://platform.moonshot.ai/console)
4. Enter the API key when prompted

The configuration in `opencode.json` sets up all default agents (build, plan, general, explore) to use the free model.

## What's Included

- Ubuntu base image
- Node.js LTS
- OpenCode AI coding agent
- Git
- Pre-configured `opencode.json` with free model setup

## Documentation

For more information on using OpenCode, visit:
- [OpenCode Documentation](https://opencode.ai/docs)
- [OpenCode GitHub](https://github.com/anomalyco/opencode)
