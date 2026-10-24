# Weather Checker

A small Python script that fetches the current temperature for two Malaysian cities from the Open-Meteo APi, then compares which one is hotter.

This is my first project on my path toward building AI agents

## Example outputs
1.09
美里现在的温度2026-10-24T12:30: 27.3
古晋现在的温度2026-10-24T12:30: 29.8
古晋比美里热

## Features
- Fetches live weather data from the free
- Stores results in a typed `Weather` dataclass
- Fetches both cities at the same time with `asyncio.gather()`, cutting the run time roughly in half (about 2.0s -> 1.0s)

## Tech
-  Python 3.15
- [uv](https://docs.astral.sh/uv/) for project and package management
- [httpx](https://www.python-httpx.org/) (async client) for HTTP requests
- [ruff](https://docs.astral.sh/ruff/) for formatting

## Getting started

```bash
git clone <your-repo-url>
cd <your-repo-folder>
uv sync
uv run main.py
```

## What I learned

- Setting up a Python project with uv
- Calling a REST API and reading nested JSON
- Using type hints and dataclasses
- The difference between `print` and `return`
- Running requests concurrently with `async` / `await` and `asyncio.gather()