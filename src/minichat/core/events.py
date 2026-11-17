from enum import Enum


class Event(str, Enum):
    CONFIG_CHANGED = "config_changed"
    GENERATING_START = "generating_start"
    GENERATING_ERROR = "generating_error"
    GENERATING_DONE = "generating_done"
    MESSAGES_UPDATED = "messages_updated"
    EXPORT_DONE = "export_done"