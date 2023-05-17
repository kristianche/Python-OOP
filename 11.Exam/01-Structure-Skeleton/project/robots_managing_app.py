from project.robots.base_robot import BaseRobot
from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
from typing import List


class RobotsManagingApp:

    possible_matches = {"MainService": "Male", "SecondaryService": "Female"}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type == "MainService":
            if name not in [s.name for s in self.services]:
                service = MainService(name)
                self.services.append(service)
                return f"{service_type} is successfully added."
        elif service_type == "SecondaryService":
            if name not in [s.name for s in self.services]:
                service = SecondaryService(name)
                self.services.append(service)
                return f"{service_type} is successfully added."
        else:
            raise Exception("Invalid service type!")

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type == "MaleRobot":
            if name not in [r.name for r in self.robots]:
                robot = MaleRobot(name, kind, price)
                self.robots.append(robot)
                return f"{robot_type} is successfully added."
        elif robot_type == "FemaleRobot":
            if name not in [r.name for r in self.robots]:
                robot = FemaleRobot(name, kind, price)
                self.robots.append(robot)
                return f"{robot_type} is successfully added."
        else:
            raise Exception("Invalid robot type!")

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = [r for r in self.robots if r.name == robot_name][0]
        service = [s for s in self.services if s.name == service_name][0]
        if isinstance(robot, MaleRobot) and isinstance(service, MainService):

            if len(service.robots) == service.capacity:
                raise Exception("Not enough capacity for this robot!")

            service.robots.append(robot)
            self.robots.remove(robot)
            return f"Successfully added {robot_name} to {service_name}."
        elif isinstance(robot, FemaleRobot) and isinstance(service, SecondaryService):
            if len(service.robots) == service.capacity:
                raise Exception("Not enough capacity for this robot!")

            service.robots.append(robot)
            self.robots.remove(robot)
            return f"Successfully added {robot_name} to {service_name}."
        else:
            return "Unsuitable service."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        if robot_name not in [r.name for r in service.robots]:
            raise Exception("No such robot in this service!")

        robot = [r for r in service.robots if r.name == robot_name][0]
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]

        for robot in service.robots:
            robot.eating()
        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        service = [s for s in self.services if s.name == service_name][0]
        total_price = 0

        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = []
        for service in self.services:
            details = service.details()
            result.append(details)

        return "\n".join(result)


main_app = RobotsManagingApp()
print(main_app.add_service('SecondaryService', 'ServiceRobotsWorld'))
print(main_app.add_service('MainService', 'ServiceTechnicalsWorld'))
print(main_app.add_robot('FemaleRobot', 'Scrap', 'HouseholdRobots', 321.26))
print(main_app.add_robot('FemaleRobot', 'Sparkle', 'FunnyRobots', 211.11))

print(main_app.add_robot_to_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.add_robot_to_service('Sparkle', 'ServiceRobotsWorld'))

print(main_app.feed_all_robots_from_service('ServiceRobotsWorld'))
print(main_app.feed_all_robots_from_service('ServiceTechnicalsWorld'))

print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))

print(main_app.remove_robot_from_service('Scrap', 'ServiceRobotsWorld'))
print(main_app.service_price('ServiceRobotsWorld'))
print(main_app.service_price('ServiceTechnicalsWorld'))

print(str(main_app))


