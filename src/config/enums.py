from .constants import STATUSES, UNITS
from enum import Enum


class OrderStatus(str, Enum):
    pending = STATUSES.PENDING.value
    completed = STATUSES.COMPLETED.value
    in_progress = STATUSES.IN_PROGRESS.value
    packed = STATUSES.PACKED.value


class Units(str, Enum):
    kg = UNITS.KG.value
    gram = UNITS.GRAM.value
    number = UNITS.NUMBER.value
