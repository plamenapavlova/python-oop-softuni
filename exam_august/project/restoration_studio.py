from project.paintings.base_painting import BasePainting

VALID_PAINTING_TYPES = ("OilArt", "WatercolorArt", "AcrylicArt")
class RestorationStudio:
    def __init__(self, name:str, painting_types:set):
        self.name = name
        self.painting_types = painting_types
        self.paintings: list[BasePainting] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not any(char.isalpha() for char in value):
            raise ValueError("Invalid name!")
        self.__name = value

    @property
    def painting_types(self):
        return self.__painting_types

    @painting_types.setter
    def painting_types(self, value):
        if not any(painting_type in VALID_PAINTING_TYPES for painting_type in value):
            raise ValueError("No valid painting types!")
        self.__painting_types = value

    def restore(self):
        count = 0
        for painting in self.paintings:
            if painting.status == "restorable":
                painting.restore()
                count += 1
        return f"Restored {count} painting/s."

    def status(self):
        total = sum(1 for painting in self.paintings if painting.status == "restorable")
        return f"<{self.name}> has {total} painting/s waiting for restoration."
