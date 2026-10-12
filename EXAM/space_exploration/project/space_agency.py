from astronauts.base_astronaut import BaseAstronaut
from astronauts.engineer_astronaut import EngineerAstronaut
from astronauts.scientist_astronaut import ScientistAstronaut
from stations.base_station import BaseStation
from stations.maintenance_station import MaintenanceStation
from stations.research_station import ResearchStation


class SpaceAgency:
    VALID_ASTRONAUT_TYPES = {
        "EngineerAstronaut": EngineerAstronaut,
        "ScientistAstronaut": ScientistAstronaut,
    }

    VALID_STATION_TYPES = {
        "MaintenanceStation": MaintenanceStation,
        "ResearchStation": ResearchStation,
    }
    def __init__(self):
        self.astronauts:list[BaseAstronaut] = []
        self.stations:list[BaseStation] = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        if astronaut_type not in self.VALID_ASTRONAUT_TYPES:
            raise ValueError("Invalid astronaut type!")
        if any(astronaut_id_number == a.id_number for a in self.astronauts):
            raise ValueError(f"{astronaut_id_number} has been already added!")

        astronaut_class = self.VALID_ASTRONAUT_TYPES[astronaut_type]
        astronaut = astronaut_class(astronaut_id_number, astronaut_salary)
        self.astronauts.append(astronaut)

        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        if station_type not in self.VALID_STATION_TYPES:
            raise ValueError("Invalid station type!")
        if any(station_name == s.name for s in self.stations):
            raise ValueError(f"{station_name} has been already added!")
        station_class = self.VALID_STATION_TYPES[station_type]
        station = station_class(station_name)
        self.stations.append(station)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station = next((s for s in self.stations if station_name == s.name), None)
        if station is None:
            raise ValueError(f"Station {station_name} does not exist!")
        astronaut = next((a for a in self.astronauts if astronaut_type == a.__class__.__name__), None)
        if astronaut is None:
            raise ValueError("No available astronauts of the type!")
        if station.capacity == 0:
            return "This station has no available capacity."
        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1
        return f"{astronaut.id_number} was assigned to {station_name}."

    def train_astronauts(self, station: BaseStation, sessions_number: int):
        for _ in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()

        total_stamina = sum(a.stamina for a in station.astronauts)
        return (
            f"{station.name} astronauts have {total_stamina} total stamina "
            f"after {sessions_number} training session/s."
        )

    def retire_astronaut(self, station: BaseStation, astronaut_id_number: str):
        astronaut = next((a for a in station.astronauts if a.id_number == astronaut_id_number), None)
        if astronaut is None or astronaut.stamina == 100:
            return "The retirement process was canceled."
        station.astronauts.remove(astronaut)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for s in self.stations:
            s.update_salaries(min_value)
        sorted_stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))
        result = [
            "*Space Agency Up-to-Date Report*",
            f"Total number of available astronauts: {len(self.astronauts)}",
            f"**Stations count: {len(self.stations)}; Total available capacity: {sum(s.capacity for s in self.stations)}**"
        ]

        for s in sorted_stations:
            result.append(s.status())

        return "\n".join(result)



