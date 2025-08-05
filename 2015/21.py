import re
from enum import Enum
from itertools import combinations
from typing import List as PyList

from pydantic import BaseModel, Field

from modules.advent_of_code import solve


class ItemType(str, Enum):
    Weapon = "weapon"
    Armor = "armor"
    Ring = "ring"


class Item(BaseModel):
    name: str
    type: ItemType
    cost: int
    damage: int
    armor: int


WEAPONS = [
    Item(name="Dagger", type=ItemType.Weapon, cost=8, damage=4, armor=0),
    Item(name="Shortsword", type=ItemType.Weapon, cost=10, damage=5, armor=0),
    Item(name="Warhammer", type=ItemType.Weapon, cost=25, damage=6, armor=0),
    Item(name="Longsword", type=ItemType.Weapon, cost=40, damage=7, armor=0),
    Item(name="Greataxe", type=ItemType.Weapon, cost=74, damage=8, armor=0),
]

ARMORS = [
    Item(name="Leather", type=ItemType.Armor, cost=13, damage=0, armor=1),
    Item(name="ChainMail", type=ItemType.Armor, cost=31, damage=0, armor=2),
    Item(name="SplintMail", type=ItemType.Armor, cost=53, damage=0, armor=3),
    Item(name="BandedMail", type=ItemType.Armor, cost=75, damage=0, armor=4),
    Item(name="PlateMail", type=ItemType.Armor, cost=102, damage=0, armor=5),
]

RINGS = [
    Item(name="Damage +1", type=ItemType.Ring, cost=25, damage=1, armor=0),
    Item(name="Damage +2", type=ItemType.Ring, cost=50, damage=2, armor=0),
    Item(name="Damage +3", type=ItemType.Ring, cost=100, damage=3, armor=0),
    Item(name="Defense +1", type=ItemType.Ring, cost=20, damage=0, armor=1),
    Item(name="Defense +2", type=ItemType.Ring, cost=40, damage=0, armor=2),
    Item(name="Defense +3", type=ItemType.Ring, cost=80, damage=0, armor=3),
]


class Player(BaseModel):
    name: str
    hit_points: int = 0
    items: PyList[Item] = Field(default_factory=list)
    cost: int = 0
    damage: int = 0
    armor: int = 0


# Start coding here
# ==========================================================================
def parse(data):
    numbers = re.findall(r"(\d+)", data)
    boss = Player(
        name="Boss",
        hit_points=int(numbers[0]),
        damage=int(numbers[1]),
        armor=int(numbers[2]),
    )
    return boss


def play_game(player: Player, boss: Player):
    player_hp = player.hit_points
    boss_hp = boss.hit_points

    while player_hp > 0 and boss_hp > 0:
        damage_to_boss = player.damage - boss.armor
        if damage_to_boss <= 0:
            damage_to_boss = 1
        boss_hp -= damage_to_boss

        if boss_hp <= 0:
            return True

        damage_to_player = boss.damage - player.armor
        if damage_to_player <= 0:
            damage_to_player = 1
        player_hp -= damage_to_player

        if player_hp <= 0:
            return False

    return False


def generate_equipment_combinations():
    """Generate all valid equipment combinations:
    - Exactly 1 weapon (required)
    - 0-1 armor pieces (optional)
    - 0-2 rings (optional)
    """
    equipment_combinations = []

    # Generate all possible armor combinations (0 or 1 armor piece)
    armor_combinations = [tuple()] + [(armor,) for armor in ARMORS]

    # Generate all possible ring combinations (0, 1, or 2 rings)
    ring_combinations = [tuple()]  # No rings
    ring_combinations.extend(combinations(RINGS, 1))  # 1 ring
    ring_combinations.extend(combinations(RINGS, 2))  # 2 rings (no duplicates)

    # Generate all equipment combinations
    for weapon in WEAPONS:
        for armor_combo in armor_combinations:
            for ring_combo in ring_combinations:
                equipment = [weapon] + list(armor_combo) + list(ring_combo)
                equipment_combinations.append(equipment)

    return equipment_combinations


def calculate_player_stats(items):
    """Calculate player stats based on equipped items"""
    total_cost = sum(item.cost for item in items)
    total_damage = sum(item.damage for item in items)
    total_armor = sum(item.armor for item in items)

    return total_cost, total_damage, total_armor


def part_one(data):
    combinations = generate_equipment_combinations()

    min_cost = float("inf")
    best_combo = None

    for combo in combinations:
        cost, damage, armor = calculate_player_stats(combo)

        player = Player(
            name="Player",
            hit_points=100,
            items=combo,
            cost=cost,
            damage=damage,
            armor=armor,
        )

        if play_game(player, data):
            if cost < min_cost:
                min_cost = cost
                best_combo = combo

    # Print detailed information about the winning combination
    print(f"Cheapest winning combination costs {min_cost} gold")
    print(f"Items: {[item.name for item in best_combo]}")
    print(f"Damage: {sum(item.damage for item in best_combo)}")
    print(f"Armor: {sum(item.armor for item in best_combo)}")

    return min_cost


def part_two(data):
    combinations = generate_equipment_combinations()

    max_cost = 0
    worst_combo = None

    for combo in combinations:
        cost, damage, armor = calculate_player_stats(combo)

        player = Player(
            name="Player",
            hit_points=100,
            items=combo,
            cost=cost,
            damage=damage,
            armor=armor,
        )

        # If player loses, check if this is the most expensive losing combination
        if not play_game(player, data):
            if cost > max_cost:
                max_cost = cost
                worst_combo = combo

    # Print detailed information about the worst combination
    if worst_combo:
        print(f"Most expensive losing combination costs {max_cost} gold")
        print(f"Items: {[item.name for item in worst_combo]}")
        print(f"Damage: {sum(item.damage for item in worst_combo)}")
        print(f"Armor: {sum(item.armor for item in worst_combo)}")

    return max_cost


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
