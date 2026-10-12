from project.paintings.base_painting import BasePainting


class OilArt(BasePainting):
    painting_type  = "OilArt"

    def __init__(self, catalogue_number: str, price: float, status: str):
        super().__init__(catalogue_number, price, status)

    def restore(self):
        if self.status == "restorable":
            self.status = "ready"
            self.price *= 2

