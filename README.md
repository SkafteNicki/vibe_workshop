# Vibe Coding Workshop

This repository is the starting point for the workshop.

When you open the Codespace, everything you need is already prepared for you. You do not need to install anything manually.

## First Steps

1. Open a terminal in Codespaces.
2. Type this and press Enter:

```bash
opencode
```

This starts OpenCode, which is the AI assistant you will use during the workshop.

## Connect Your Model Provider

To let OpenCode talk to an AI model, connect it to OpenRouter.

1. Open the OpenRouter dashboard.
2. Click `Create API Key`.
3. Copy the API key.
4. In OpenCode, type:

```text
/connect
```

5. Search for `OpenRouter`.
6. Paste the API key when asked.

```text
┌ API key
│
│
└ enter
```

## Pick A Model

OpenCode can work with many different models.

If you want to choose one yourself, type:

```text
/models
```

You can also see available models from the terminal with:

```bash
opencode models
```

## Default Model Setup In This Workshop

This workshop already includes a default setup in `opencode.json`.

- The `plan` agent uses `openrouter/anthropic/claude-sonnet-4.6`
- The `build` agent uses `openrouter/anthropic/claude-sonnet-4.6`

In practice, this means the workshop already points important OpenCode tasks to Sonnet by default.

## What Is Already Included

Your Codespace already includes:

- OpenCode
- Pi
- Node.js
- Python
- uv
- Pyright
- Git

## If You Get Stuck

That is normal.

The goal of the workshop is not to memorize commands. The goal is to practice working with AI tools in a calm, hands-on way.

## References

- [OpenCode Documentation](https://opencode.ai/docs)
- [OpenCode GitHub](https://github.com/anomalyco/opencode)
