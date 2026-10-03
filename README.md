# Jarvis Assistant

A lightweight Jarvis-style assistant built in Python for local experimentation, command-line interaction, and small project tooling.

## What this project includes

- A Python CLI assistant with a friendly terminal interface
- A local fallback mode when no external AI service is configured
- Optional OpenAI-backed behavior when an API key is set
- A small ant colony simulation project kept in a separate repository

## Project structure

- `src/jarvis_assistant/` — main assistant package
- `tests/` — project tests
- `ant-sim/` — separate project that is intentionally kept out of the main repo

## Features

- Local command-line assistant
- Optional OpenAI integration when an API key is configured
- Readable terminal responses and simple CLI usage
- Easy setup for experimentation and extension

## Quick start

1. Create and activate a virtual environment if needed.
2. Install the project:

   ```bash
   python -m pip install -e .
   ```

3. Run the assistant:

   ```bash
   jarvis "Hello there"
   ```

   or:

   ```bash
   python -m jarvis_assistant
   ```

## Optional OpenAI setup

Create a `.env` file with:

```bash
OPENAI_API_KEY=your_key_here
```

If an API key is present and the `openai` package is available, the assistant will try to use it. Otherwise it falls back to a built-in local response mode.

## Notes

This project is designed for lightweight local use and experimentation. It is intentionally simple and easy to extend as a personal assistant or prototype project.
