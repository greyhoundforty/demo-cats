# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Setup

This is a Python project using Python 3.12 with mise for environment management. The project uses a virtual environment located at `.venv/`.

## Development Commands

The project uses mise with custom tasks defined in `.mise.toml`:

- `mise run uv:reqs` (alias: `mise run uvr`) - Install dependencies from requirements.txt using uv
- `mise run uv:freeze` (alias: `mise run uvf`) - Create requirements.txt from currently installed packages
- `mise run uv:install` (alias: `mise run uvi`) - Install pip packages using uv
- `mise run info` - Print project information (name and virtual environment path)

## Architecture

This is a minimal Python project with:
- `app.py` - Main application file (currently empty)
- `Dockerfile` - Container configuration (currently empty)
- `.mise.toml` - Environment and task configuration
- `.venv/` - Python virtual environment directory

The project appears to be in early development stages with placeholder files ready for implementation.