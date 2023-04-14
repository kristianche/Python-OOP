from project.services.base_service import BaseService


class MainService(BaseService):
    CAPACITY = 30

    def __init__(self, name: str):
        self.name = name
        super().__init__(self.name, MainService.CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Main Service:\n" \
                   f"Robots: none"

        return f"{self.name} Main Service:\n" \
               f"Robots: {' '.join([str(r.name) for r in self.robots])}"
