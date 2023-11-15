"""
This is the entry point for the HeyGPT API.
"""

import logging
import sys
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from routes.chat import ChatRouter

logger = logging.getLogger("uvicorn")

application = FastAPI()

application.include_router(ChatRouter)

application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)