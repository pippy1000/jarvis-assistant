# Jarvis Assistant

A lightweight Jarvis-style assistant built in Python.

## Features

- Local command-line assistant
- Optional OpenAI integration when an API key is configured
- Friendly, readable terminal output

## Quick start

1. Create a virtual environment if needed.
2. Install the project:

   python -m pip install -e .

3. Run the assistant:

   jarvis "Hello there"

   or

   python -m jarvis_assistant

## Optional OpenAI setup

Create a `.env` file with:

```bash
OPENAI_API_KEY=your_key_here
```

If an API key is present and the `openai` package is available, the assistant will try to use it. Otherwise it falls back to a built-in local response mode.
