from typing import List
from project.band import Band
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist


class ConcertTrackerApp:
    VALID_MUSICIANS = ["Guitarist", "Drummer", "Singer"]

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Musician] = []
        self.concerts: List[Concert] = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in ConcertTrackerApp.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        if name in [m.name for m in self.musicians]:
            raise Exception(f"{name} is already a musician!")

        if musician_type == "Guitarist":
            musician = Guitarist(name, age)
            self.musicians.append(musician)
        elif musician_type == "Drummer":
            musician = Drummer(name, age)
            self.musicians.append(musician)
        elif musician_type == "Singer":
            musician = Singer(name, age)
            self.musicians.append(musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if name in [b.name for b in self.bands]:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        if place in [c.place for c in self.concerts]:
            concert = next(filter(lambda c: c.place == place, self.concerts))
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        if musician_name not in [m.name for m in self.musicians]:
            raise Exception(f"{musician_name} isn't a musician!")

        if band_name not in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")

        band = next(filter(lambda b: b.name == band_name, self.bands))
        musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        band.members.append(musician)
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        if band_name not in [b.name for b in self.bands]:
            raise Exception(f"{band_name} isn't a band!")
        band = next(filter(lambda b: b.name == band_name, self.bands))
        if musician_name not in [m.name for m in band.members]:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        musician = next(filter(lambda m: m.name == musician_name, self.musicians))
        band.members.remove(musician)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        singers = [m for m in band.members if isinstance(m, Singer)]
        drummers = [m for m in band.members if isinstance(m, Drummer)]
        guitarists = [m for m in band.members if isinstance(m, Guitarist)]

        if len(singers) == 0 or len(drummers) == 0 or len(guitarists) == 0:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        are_singers_qualified = True
        for singer in singers:
            if concert.genre == "Rock":
                if "sing high pitch notes" not in singer.skills:
                    are_singers_qualified = False
            elif concert.genre == "Metal":
                if "sing low pitch notes" not in singer.skills:
                    are_singers_qualified = False
            else:
                if "sing high pitch notes" not in singer.skills or "sing low pitch notes" not in singer.skills:
                    are_singers_qualified = False

        are_drummers_qualified = True
        for drummer in drummers:
            if concert.genre == "Rock":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummers_qualified = False
            elif concert.genre == "Metal":
                if "play the drums with drumsticks" not in drummer.skills:
                    are_drummers_qualified = False
            else:
                if "play the drums with drum brushes" not in drummer.skills:
                    are_drummers_qualified = False

        are_guitarists_qualified = True
        for guitarist in guitarists:
            if concert.genre == "Rock":
                if "play rock" not in guitarist.skills:
                    are_guitarists_qualified = False
            elif concert.genre == "Metal":
                if "play metal" not in guitarist.skills:
                    are_guitarists_qualified = False
            else:
                if "play jazz" not in guitarist.skills:
                    are_guitarists_qualified = False

        if not are_guitarists_qualified or not are_drummers_qualified or not are_singers_qualified:
            raise Exception(f"The {band.name} band is not ready to play at the concert!")

        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."






