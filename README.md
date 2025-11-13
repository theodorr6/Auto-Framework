# Automation-Framework — Evoke Assignment (Python)

This repository contains a minimal Python Selenium test suite that implements the requested flows for the Evoke automation assignment. The aim is to be concise and follow the assignment requirements (POM, explicit waits, clear test structure).

Prerequisites
- Python 3.8+
- A WebDriver (e.g., chromedriver) available on PATH or configured by your driver fixture.


Create new venv
```bash
python -m venv venv_name
```

Activate venv on MacOs/Linux
```bash
source .venv/bin/activate
```

Activate venv on Windows
```bash
venv_name\Scripts\activate.bat
```

Install requirements

```bash
python -m pip install -r requirements.txt
```

Run tests

- Run the full suite:

```bash
pytest -q
```

- Run a single test example:

```bash
pytest -k test_login_success (add -s to display console output)
```

