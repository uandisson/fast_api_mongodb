from .exception import ServerBaseException


class DocumentNotFoundError(ServerBaseException):
    def __init__(self, key: dict):
        self.key = key


class DuplicateKeyError(ServerBaseException):
    pass
