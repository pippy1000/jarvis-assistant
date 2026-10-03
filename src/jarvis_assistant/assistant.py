from __future__ import annotations

import os
from datetime import datetime


class JarvisAssistant:
    """Simple assistant with a local fallback and optional OpenAI integration."""

    def __init__(self, name: str = "Jarvis") -> None:
        self.name = name

    def respond(self, prompt: str) -> str:
        text = (prompt or "").strip()
        if not text:
            return "I’m ready. Ask me for help, a summary, or a quick plan."

        lowered = text.lower()

        if "hello" in lowered or "hi" in lowered or "hey" in lowered:
            return f"Hello! I’m {self.name}. How can I help you today?"

        if "time" in lowered:
            return f"The current time is {datetime.now().strftime('%H:%M:%S')}"

        if "date" in lowered:
            return f"Today is {datetime.now().strftime('%A, %B %d, %Y')}."

        if "plan" in lowered or "task" in lowered:
            return (
                "Here’s a simple plan: 1) define the goal, 2) break it into steps, "
                "3) execute one step at a time, and 4) review results before moving on."
            )

        if "help" in lowered:
            return (
                "I can help with planning, quick summaries, task tracking, and basic guidance. "
                "Try asking for a to-do list, a summary, or a quick answer."
            )

        if os.getenv("OPENAI_API_KEY"):
            try:
                from openai import OpenAI

                client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
                response = client.responses.create(
                    model="gpt-4o-mini",
                    input=[{"role": "user", "content": text}],
                )
                return response.output_text.strip() or self._fallback_response(text)
            except Exception:
                return self._fallback_response(text)

        return self._fallback_response(text)

    def _fallback_response(self, prompt: str) -> str:
        cleaned = prompt.strip()
        if not cleaned:
            return "I’m ready when you are."
        return (
            f"I understand you want help with: '{cleaned}'. "
            "I’m in local mode right now, so I can provide quick guidance, structure, and planning support."
        )

    def chat(self) -> None:
        print(f"{self.name} is ready. Type 'exit' to quit.")
        while True:
            try:
                user_input = input("You: ")
            except KeyboardInterrupt:
                print("\nSession ended.")
                break

            if user_input.strip().lower() in {"exit", "quit", "bye"}:
                print(f"{self.name}: Goodbye.")
                break

            print(f"{self.name}: {self.respond(user_input)}")
