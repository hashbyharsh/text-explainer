from enum import Enum

class VehicleType(str, Enum):
    TRUCKS = "TRUCKS"
    BUSES = "BUSES"
    TRACTORS = "TRACTORS"
    THREE_WHEELERS = "THREE_WHEELERS"