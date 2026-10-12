from project.paintings.base_painting import BasePainting
from project.restoration_studio import RestorationStudio

from project.paintings.oil_art import OilArt
from project.paintings.watercolor_art import WatercolorArt
from project.paintings.acrylic_art import AcrylicArt

PAINTING_TYPES = {
    "OilArt": OilArt,
    "WatercolorArt": WatercolorArt,
    "AcrylicArt": AcrylicArt,
}

class ArtManager():
    def __init__(self):
        self.paintings: list[BasePainting] = []
        self.restoration_studios: list[RestorationStudio] = []

    def add_painting(self, painting_type: str, catalogue_number: str, price: float, status: str):
        if painting_type not in PAINTING_TYPES:
            raise ValueError("Invalid painting type!")

        painting = PAINTING_TYPES[painting_type](catalogue_number, price, status)
        self.paintings.append(painting)
        return f"{painting_type} <{catalogue_number}> has been added."

    def add_restoration_studio(self, name: str, painting_types: set):
        studio = RestorationStudio(name, painting_types)
        self.restoration_studios.append(studio)
        return f"{name} has been added as a restoration studio."

    def send_for_restoration(self, restoration_studio_name: str, painting_type: str):
        studio = next(s for s in self.restoration_studios if s.name == restoration_studio_name)

        if painting_type not in studio.painting_types:
            return "The studio cannot restore this painting type."

        painting = next(
            (p for p in self.paintings if type(p).painting_type == painting_type and p.status == "restorable"),
            None)

        if painting is None:
            return f"There is no eligible {painting_type}."


        self.paintings.remove(painting)
        studio.paintings.append(painting)
        return f"<{painting.catalogue_number}> was sent for restoration to {restoration_studio_name}."

    def process_restorations(self, restoration_studio: RestorationStudio):
        restorable_count = sum(1 for p in restoration_studio.paintings if p.status == "restorable")

        restoration_studio.restore()

        restored_paintings = [p for p in restoration_studio.paintings if p.status == "ready"]
        for painting in restored_paintings:
            restoration_studio.paintings.remove(painting)
            self.paintings.append(painting)

        return f"Restored {restorable_count} painting/s."

    def remove_paintings(self):
        irreparable = [p for p in self.paintings if p.status == "irreparable"]
        count = 0
        for p in irreparable:
            self.paintings.remove(p)
            count += 1

        return f"Removed {count} irreparable painting/s."

    def exhibit_paintings(self):
        ready_paintings = [p for p in self.paintings if p.is_ready]


        if not ready_paintings:
            return "Exhibition postponed!"

        ready_paintings.sort(key=lambda p: int(p.catalogue_number))

        lines = ["Art Exhibition:"]
        for painting in ready_paintings:
            lines.append(f"<{painting.catalogue_number}> {type(painting).painting_type} {painting.price:.2f}EUR")

        return "\n".join(lines)

    def manager_status(self):
        ready_count = sum(1 for p in self.paintings if p.status == "ready")
        restorable_count = sum(1 for p in self.paintings if p.status == "restorable")
        irreparable_count = sum(1 for p in self.paintings if p.status == "irreparable")

        lines = [
            "|Art Manager|",
            f"Ready-to-display paintings: {ready_count}",
            f"Need restoration paintings: {restorable_count}",
            f"Irreparable paintings: {irreparable_count}",
            f"Restoration studios: {len(self.restoration_studios)}",
        ]

        sorted_studios = sorted(
            self.restoration_studios,
            key=lambda s: (-sum(1 for p in s.paintings if p.status == "restorable"), s.name)
        )
        for studio in sorted_studios:
            lines.append(studio.status())

        return "\n".join(lines)






