#!/usr/bin/env python3
"""Command-driven, offline simulator for the repo's synthetic lessons.

This is deliberately not an LLM agent or a real cyber range. It performs only
prewritten simulations from ai_tutor.py: no shell execution, networking,
filesystem operations, credentials, or live targets. A learner's `run` command
approves the named synthetic lesson(s); each simulated step is printed.
"""

from __future__ import annotations

import re
import sys
from typing import List

from ai_tutor import SCENARIOS, TOPICS


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def resolve_topic(query: str) -> str:
    """Resolve a number or an unambiguous topic name; never execute free text."""
    query = query.strip()
    if query.isdigit():
        index = int(query) - 1
        if 0 <= index < len(TOPICS):
            return TOPICS[index]
        raise ValueError("Topic number must be from 1 to 22.")

    normalized = normalize(query)
    exact = [topic for topic in TOPICS if normalize(topic) == normalized]
    if exact:
        return exact[0]

    matches = [topic for topic in TOPICS if normalized and normalized in normalize(topic)]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        choices = ", ".join(f"{i + 1}: {name}" for i, name in enumerate(matches))
        raise ValueError(f"That topic is ambiguous. Choose its number: {choices}")
    raise ValueError("No matching lesson. Use 'list' to see valid topics.")


def run_lesson(topic: str) -> None:
    scenario = SCENARIOS[topic]
    print(f"\n=== SIMULATION: {topic} ===")
    print("Scope: fictional lesson data only; no real target or system is accessed.")
    print("Step 1 — Scenario data:")
    for key, value in scenario["synthetic_data"].items():
        print(f"  {key}: {value}")
    print("Step 2 — Simulated lesson:")
    print(f"  {scenario['simulation']}")
    print("Step 3 — Defensive actions:")
    for mitigation in scenario["mitigations"]:
        print(f"  - {mitigation}")
    print("Step 4 — Result: synthetic scenario reviewed; no real-world action taken.")
    print(f"ACTIVITY LOG: completed simulation '{topic}'")


def help_text() -> None:
    print("""
Commands (only these are accepted):
  list                 Show the 22 available lessons
  run <number|topic>   Run one prewritten synthetic simulation
  run all              Run every prewritten synthetic simulation
  secure <number|topic> Show the defensive recommendations for a lesson
  help                 Show this help
  exit                 Quit

Examples:
  run 12
  run WiFi WPA/WPA2
  secure 17

The simulator does not interpret commands as shell or AI instructions.
""")


def main() -> int:
    print("Offline Synthetic Cybersecurity Lesson Simulator")
    print("Your command can start a lesson; the simulator only runs allowlisted, prewritten scenarios.")
    print("No real Wi-Fi, network, account, file, or host action is performed. Type 'help'.")

    while True:
        try:
            command = input("\nsandbox> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nStopped.")
            return 0

        if not command:
            continue
        if command.lower() in {"exit", "quit"}:
            print("Stopped.")
            return 0
        if command.lower() == "help":
            help_text()
            continue
        if command.lower() == "list":
            for i, topic in enumerate(TOPICS, 1):
                print(f"{i:2}. {topic}")
            continue

        action, _, target = command.partition(" ")
        action = action.lower()
        if action not in {"run", "secure"} or not target.strip():
            print("Command not recognized. Use 'help'; arbitrary commands are not executed.")
            continue

        if action == "run" and normalize(target) == "all":
            print("Running the requested batch of synthetic lessons. Press Ctrl-C to stop.")
            try:
                for topic in TOPICS:
                    run_lesson(topic)
            except KeyboardInterrupt:
                print("\nBatch stopped by learner.")
            continue

        try:
            topic = resolve_topic(target)
        except ValueError as exc:
            print(exc)
            continue

        if action == "run":
            run_lesson(topic)
        else:
            print(f"\nDefensive recommendations — {topic}")
            for item in SCENARIOS[topic]["mitigations"]:
                print(f"- {item}")
            print("No system changes were made.")


if __name__ == "__main__":
    sys.exit(main())
