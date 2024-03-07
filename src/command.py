from __future__ import annotations
from enum import Enum

class Command:
    def __init__(self, command_type_value: CommandType, value: int = None):
        self.command_type = CommandType(command_type_value)
        self.value = value
        
    def __repr__(self) -> str:
        return f"{self.command_type.name}, value: {self.value}"
        
class CommandType(Enum):
    MOVE_FORWARD = 'fd'
    MOVE_BACKWARDS = 'bk'
    RIGHT_TURN = 'rt'
    LEFT_TURN = 'lt'
    PEN_DOWN = 'pendown'
    PEN_UP = 'penup'