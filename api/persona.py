"""
The persona module contains the persona class and the user class for defining
the data structures used in the chatbot.
"""

from __future__ import annotations

import logging

from dataclasses import dataclass, field

from util import fs, info
from language.inference import inference

logger = logging.getLogger("uvicorn")

@dataclass
class User:
    """
    A user represents a user who can interact with the chatbot.
    They can be loaded from and saved to a JSON file.
    """
    name: str
    history: list[dict[str, str]] = field(default_factory=list)

    def __str__(self) -> str:
        lines = [
            "Here is a description of the user:",
            f"The user's name is {self.name}."
            "The user is a human."
        ]
        return "\n".join(lines)
    
    def history_to_text(self) -> str:
        """Convert the history to text."""
        text = ""
        for interaction in self.history:
            text += f"<|user|>{interaction['user']}\n<|model|>{interaction['model']}\n"
        return text
    
    def add_historical_interaction(self, user: str, model: str) -> None:
        """Add a historical interaction to the user's history."""
        self.history.append({"user": user, "model": model})
    
    @classmethod
    def load_name(cls, username: str) -> User:
        """Load the user from the filesystem."""
        history = fs.load_user_history(username) or []
        return cls(username, history)
    
    def save(self) -> None:
        """Save the user to the filesystem."""
        fs.save_user_history(self.name, self.history)
    

class Persona:
    def __init__(self, name: str):
        self.name = name
        # Get the date and time in a human-readable format
        self.instructions = fs.load_instructions({"name": self.name})
        self.persona_name, self.persona = fs.load_persona(name)

    def listen(self, user: User, message: str) -> str:
        """Listen to the user and respond if necessary."""
        # For now, any message will trigger a response
        # Create the inference prompt to use, based on the
        # instructions, persona, and the User
        fmessage = f"<|user|>{message}\n<|model|>"
        prompt = '\n'.join([self.instructions, self.persona, str(user), user.history_to_text(), f"<|user|>{info.get_datetime()}", fmessage])
        logger.debug(f"Prompt: {prompt}")
        reply = inference(prompt).strip()
        user.add_historical_interaction(message, reply)
        return reply

