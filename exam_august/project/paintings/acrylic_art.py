from project.paintings.base_painting import BasePainting


class AcrylicArt(BasePainting):
    painting_type = "AcrylicArt"

    def __init__(self, catalogue_number: str, price: float, status: str):
        super().__init__(catalogue_number, price, status)

    def restore(self):
        if self.status == "restorable":
            self.status = "ready"
            self.price += 1000.0

