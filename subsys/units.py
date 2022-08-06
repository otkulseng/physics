
class Unit:
    units = "m/s^2"
    def __init__(self, units) -> None:
        self.units = units


class Constant:
    descr = "Name of constant"
    value = 1.0
    unit = Unit("m")

    def __init__(self, value, unit, descr="") -> None:
        self.value = value
        self.unit = unit
        self.descr = descr