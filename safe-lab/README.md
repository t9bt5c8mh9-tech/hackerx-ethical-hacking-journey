# Command-driven offline lesson simulator

This folder provides a small, command-driven educational simulator for all 22 README topics. `command_runner.py` runs prewritten synthetic scenarios; your command starts a lesson or batch, and the simulator prints each step and its defensive takeaways.

## Run

From this directory:

```bash
python3 command_runner.py
```

Examples:

```text
sandbox> run 12
sandbox> run WiFi WPA/WPA2
sandbox> secure 17
sandbox> run all
```

`run all` starts the full synthetic lesson batch. Press Ctrl-C to stop it.

## Scope and limits

This is an **offline simulator**, not an AI model and not an operating-system sandbox or real cyber range. It has no network client, shell execution, arbitrary code execution, credential access, or file-writing logic. It only displays the lesson data and descriptions in `ai_tutor.py`. The Wi-Fi lessons model fictional configuration and defensive recommendations; they do not create an access point, capture traffic, or crack passwords.

The command parser accepts only `list`, `run`, `secure`, `help`, and `exit`. A command outside that allowlist is rejected, not passed to a shell or model. Review the code before running it. For stronger isolation, run it in a disposable VM/container with networking disabled.
