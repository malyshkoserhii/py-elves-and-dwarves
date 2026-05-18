from app.players.dwarves.dwarf_blacksmith import DwarfBlacksmith
from app.players.dwarves.dwarf_warrior import DwarfWarrior
from app.players.elves.druid import Druid
from app.players.elves.elf_ranger import ElfRanger


type PlayersListType = list[DwarfBlacksmith | DwarfWarrior | Druid | ElfRanger]


def calculate_team_total_rating(players: PlayersListType) -> int:
    ratings = [player.get_rating() for player in players]
    return sum(ratings)


def elves_concert(elves: list[Druid, ElfRanger]) -> None:
    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list[DwarfWarrior, DwarfBlacksmith]) -> None:
    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
