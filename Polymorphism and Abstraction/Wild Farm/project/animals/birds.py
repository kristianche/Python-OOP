from project.animals.animal import Bird


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"




class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"