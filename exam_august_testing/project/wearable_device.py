from typing import Tuple, Optional


class WearableDevice:
    def __init__(self,
                 model: str,
                 cost: float,
                 resolution: Tuple[int, int],
                 is_operating: bool = True,
                 battery_life: Optional[int] = None):
        self.model = model
        self.cost = cost
        self.resolution = resolution
        self.is_operating = is_operating
        self.battery_life = battery_life

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip() or len(value.strip()) > 40:
            raise ValueError("Model must be a non-empty string up to 40 characters!")
        self.__model = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if value < 1.0:
            raise ValueError("Cost must be at least 1.0!")
        self.__cost = value

    @property
    def resolution(self):
        return self.__resolution

    @resolution.setter
    def resolution(self, value):
        if len(value) != 2:
            raise ValueError("Resolution must be a tuple of (width, height)!")
        if any(dim <= 0 for dim in value):
            raise ValueError("Resolution dimensions must be positive integers!")
        self.__resolution = value

    @property
    def battery_life(self):
        return self.__battery_life

    @battery_life.setter
    def battery_life(self, value):
        if value is not None and (value < 0 or value > 100):
            raise ValueError("Battery life must be between 0 and 100 hours!")
        self.__battery_life = value

    def get_operational_status(self):
        return f"Model: {self.model} is currently {'operational' if self.is_operating else 'not operational'}."

    def get_info(self):
        width, height = self.resolution
        battery = f"{self.battery_life}h" if self.battery_life is not None else "unknown"
        return (f"{self.model} display resolution: {width}x{height} pixels | "
                f"Battery life: {battery}")
