"""
The util.fs module contains the file system utilities for HeyGPT which
are used to load and save data.
"""

from __future__ import annotations

import os
import pathlib as pl
import logging
import json

from jinja2 import FileSystemLoader, Environment

logger = logging.getLogger("uvicorn")

SettingsDirectory = pl.Path("/app/settings") if pl.Path("/app/settings").exists() else pl.Path("settings")
CacheDirectory = pl.Path("/app/cache") if pl.Path("/app/cache").exists() else pl.Path("cache")
if not SettingsDirectory.exists():
    logger.warning("Could not find settings directory. Creating...")
    os.mkdir(SettingsDirectory)
if not CacheDirectory.exists():
    logger.warning("Could not find cache directory. Creating...")
    os.mkdir(CacheDirectory)


def load_instructions(data: dict) -> str | None:
    """Load the instruct text."""
    logger.debug("Loading Instruct Text...")
    try:
        template = Environment(loader=FileSystemLoader(SettingsDirectory)).get_template('instruct.j2')
        return template.render(data)
    except FileNotFoundError:
        logger.error("Could not find instruct.j2")

def load_persona(name: str) -> (str, str) | None:
    """Get the persona for the chatbot."""
    logger.debug(f"Loading Persona '{name}'...")
    filepath = SettingsDirectory / f"{name.lower()}.ai"
    try:
        with open(filepath, "r") as f:
            return name, f.read()
    except FileNotFoundError:
        logger.error(f"Could not find persona '{name}' file.")

def load_user_history(username: str) -> list[dict[str, str]] | None:
    """Load the user history."""
    filepath = CacheDirectory / f"{username.lower()}.json"
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Could not find user history for '{username}'.")

def save_user_history(username: str, history: list[dict[str, str]]) -> None:
    """Save the user history."""
    filepath = CacheDirectory / f"{username.lower()}.json"
    try:
        with open(filepath, "w") as f:
            json.dump(history, f)
    except json.JSONDecodeError:
        logger.error(f"Could not save user history for '{username}'.")