"""
The info module contains functions for querying for extra information about the
world for the model to use in a conversation.
"""

from __future__ import annotations

import logging
import datetime

logger = logging.getLogger("uvicorn")

def get_datetime() -> str:
    """Get the date and time in a human-readable format."""
    now = datetime.datetime.now()
    stamp = now.strftime("%A, %B %d, %Y at %I:%M %p")
    logger.info(f"Got date and time: {stamp}")
    return f"It is currently {stamp}."