

import os
import logging

from fastapi import APIRouter
from pydantic import BaseModel

from persona import Persona, User

logger = logging.getLogger("uvicorn")

PERSONA = os.getenv("HEY_PERSONA", "Jai")

ChatRouter = APIRouter(prefix="/chat")

class Message(BaseModel):
    """A message from a user."""
    sender_name: str
    message: str


@ChatRouter.post('/message')
def send_message(message: Message) -> Message:
    """Send a message to the chatbot."""
    logger.info(f"Received message from {message.sender_name}: {message.message}")
    persona = Persona(PERSONA)
    user = User.load_name(message.sender_name)
    reply = persona.listen(user, message.message)
    user.save()
    logger.info(f"Sending message to {message.sender_name}: {reply}")
    return Message(sender_name=persona.name, message=reply)