from project.services.base_service import BaseService


class SecondaryService(BaseService):
    CAPACITY = 15

    def __init__(self, name: str):
        self.name = name
        super().__init__(self.name, SecondaryService.CAPACITY)

    def details(self):
        if not self.robots:
            return f"{self.name} Secondary Service:\n" \
                   f"Robots: none"

        return f"{self.name} Secondary Service:\n" \
               f"Robots: {' '.join([str(r.name) for r in self.robots])}"