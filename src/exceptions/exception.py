from typing import Optional


class ServerBaseException(Exception):
    error_message: Optional[str]

    def __init__(self, error_message: str = ""):
        self.error_message = error_message
