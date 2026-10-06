# ⌨️ Python Keyboard Event Logger

A transparent, consent-based Python project for studying keyboard event capture, timestamped local logging, modular application design, testing, and CI.

> **Authorization notice:** Run this only on a device and user session you own or are explicitly authorized to monitor. This repository intentionally does not include stealth, persistence, credential theft, remote exfiltration, or evasion features.

## Features

- Keyboard event capture with `pynput`
- UTC timestamped local event storage
- Modular CLI, formatting, configuration, and storage components
- Configurable log path via environment variable
- Graceful handling of special keys
- Automated pytest suite
- GitHub Actions CI
- Explicit security policy

## Architecture

```text
Keyboard Event
      |
      v
pynput Listener
      |
      v
format_key()
      |
      v
EventStore
      |
      v
Local Timestamped Log
```

## Project structure

```text
.
├── logger/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── formatting.py
│   └── storage.py
├── tests/
│   ├── test_formatting.py
│   └── test_storage.py
├── .github/workflows/ci.yml
├── .env.example
├── .gitignore
├── SECURITY.md
├── requirements.txt
├── main.py
└── run.py
```

## Run

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
python run.py
```

The logger writes to `logs/keystrokes.log` by default.

## Configure

Set `KEYLOGGER_LOG_FILE` before launching:

```text
KEYLOGGER_LOG_FILE=logs/research.log
```

## Test

```bash
pytest -q
```

## SOC / Security value

This project demonstrates endpoint telemetry concepts including event collection, timestamping, local log storage, input-monitoring architecture, Python modularization, testing, and CI. For a SOC portfolio, it is best presented as a controlled research artifact for understanding endpoint telemetry and detection opportunities, not as a covert collection utility.

## Limitations

Keyboard monitoring has serious privacy implications and can trigger endpoint security controls. The implementation intentionally stays local and does not attempt to bypass security controls or transmit captured data.

## Defensive roadmap

A stronger next iteration would add a synthetic keyboard-event generator and a small detection dashboard that demonstrates how defensive tooling can identify suspicious input-monitoring behavior without recording real user input.

## License

MIT
