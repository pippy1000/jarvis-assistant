from __future__ import annotations

import argparse

from .assistant import JarvisAssistant


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the Jarvis assistant.")
    parser.add_argument("prompt", nargs="?", help="Prompt to send to the assistant")
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Start the interactive chat loop",
    )
    args = parser.parse_args()

    assistant = JarvisAssistant()

    if args.interactive or not args.prompt:
        assistant.chat()
        return

    print(assistant.respond(args.prompt))


if __name__ == "__main__":
    main()
