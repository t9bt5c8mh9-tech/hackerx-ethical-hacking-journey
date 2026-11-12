# Safe Sandbox AI Tutor

This folder contains a local, synthetic-only learning scaffold for the cybersecurity topics in the repository README.

## What it does

- Shows a list of all 22 topics
- Explains each topic using fictional data and a safe educational simulation
- Requires you to type `yes` before any simulation continues
- Shows the recommended mitigations and keeps the learning environment sandboxed
- Does not touch your real filesystem, credentials, networks, or public systems

## How to run

```bash
cd safe-lab
python3 ai_tutor.py
```

## Example

```text
Select a topic number (1-22), type 'all' for all topics, or 'exit': 11
```

This opens the Wi-Fi lesson using synthetic data only.

## Safety rules

- Use this script only inside a disposable local lab or VM
- Never point it at real Wi-Fi, hosts, or public systems
- Keep all materials synthetic and sandboxed
- Human approval is required before each simulation continues
- Treat the output as educational content, not a real-world attack workflow

