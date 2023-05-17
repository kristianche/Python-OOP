from project.band_members.musician import Musician


class Guitarist(Musician):

    SKILLS_THAT_CAN_BE_LEARNT = ["play metal", "play rock", "play jazz"]

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        super().__init__(self.name, self.age)

    def learn_new_skill(self, new_skill: str):
        if new_skill not in Guitarist.SKILLS_THAT_CAN_BE_LEARNT:
            raise ValueError(f"{new_skill} is not a needed skill!")

        if new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")

        self.skills.append(new_skill)
        return f"{self.name} learned to {new_skill}."