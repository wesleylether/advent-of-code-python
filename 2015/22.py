import heapq

from modules.advent_of_code import solve


# Start coding here
# ==========================================================================


class GameState:
    def __init__(
        self,
        player_hp=50,
        player_mana=500,
        boss_hp=55,
        boss_damage=8,
        shield_timer=0,
        poison_timer=0,
        recharge_timer=0,
        mana_spent=0,
        hard_mode=False,
    ):
        self.player_hp = player_hp
        self.player_mana = player_mana
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.shield_timer = shield_timer
        self.poison_timer = poison_timer
        self.recharge_timer = recharge_timer
        self.mana_spent = mana_spent
        self.hard_mode = hard_mode

    def copy(self):
        return GameState(
            self.player_hp,
            self.player_mana,
            self.boss_hp,
            self.boss_damage,
            self.shield_timer,
            self.poison_timer,
            self.recharge_timer,
            self.mana_spent,
            self.hard_mode,
        )

    def apply_effects(self):
        # Shield effect
        if self.shield_timer > 0:
            self.shield_timer -= 1

        # Poison effect
        if self.poison_timer > 0:
            self.boss_hp -= 3
            self.poison_timer -= 1

        # Recharge effect
        if self.recharge_timer > 0:
            self.player_mana += 101
            self.recharge_timer -= 1

    def can_cast_spell(self, spell):
        spells = {
            "magic_missile": 53,
            "drain": 73,
            "shield": 113,
            "poison": 173,
            "recharge": 229,
        }

        if self.player_mana < spells[spell]:
            return False

        if spell == "shield" and self.shield_timer > 0:
            return False
        if spell == "poison" and self.poison_timer > 0:
            return False
        if spell == "recharge" and self.recharge_timer > 0:
            return False

        return True

    def cast_spell(self, spell):
        if spell == "magic_missile":
            self.player_mana -= 53
            self.mana_spent += 53
            self.boss_hp -= 4
        elif spell == "drain":
            self.player_mana -= 73
            self.mana_spent += 73
            self.boss_hp -= 2
            self.player_hp += 2
        elif spell == "shield":
            self.player_mana -= 113
            self.mana_spent += 113
            self.shield_timer = 6
        elif spell == "poison":
            self.player_mana -= 173
            self.mana_spent += 173
            self.poison_timer = 6
        elif spell == "recharge":
            self.player_mana -= 229
            self.mana_spent += 229
            self.recharge_timer = 5

    def boss_turn(self):
        armor = 7 if self.shield_timer > 0 else 0
        damage = max(1, self.boss_damage - armor)
        self.player_hp -= damage

    def is_player_dead(self):
        return self.player_hp <= 0

    def is_boss_dead(self):
        return self.boss_hp <= 0


def find_min_mana(initial_state):
    # Priority queue: (mana_spent, counter, state)
    pq = [(0, 0, initial_state)]
    visited = set()
    counter = 1

    while pq:
        mana_spent, _, state = heapq.heappop(pq)

        # Create state key for visited check
        state_key = (
            state.player_hp,
            state.player_mana,
            state.boss_hp,
            state.shield_timer,
            state.poison_timer,
            state.recharge_timer,
        )

        if state_key in visited:
            continue
        visited.add(state_key)

        # Player turn
        new_state = state.copy()

        # Hard mode: player loses 1 HP at start of turn
        if new_state.hard_mode:
            new_state.player_hp -= 1
            if new_state.is_player_dead():
                continue

        # Apply effects
        new_state.apply_effects()

        # Check if boss is dead after effects
        if new_state.is_boss_dead():
            return new_state.mana_spent

        # Try each spell
        spells = ["magic_missile", "drain", "shield", "poison", "recharge"]
        for spell in spells:
            if new_state.can_cast_spell(spell):
                spell_state = new_state.copy()
                spell_state.cast_spell(spell)

                # Check if boss is dead after spell
                if spell_state.is_boss_dead():
                    return spell_state.mana_spent

                # Boss turn
                boss_state = spell_state.copy()
                boss_state.apply_effects()

                # Check if boss is dead after effects
                if boss_state.is_boss_dead():
                    return boss_state.mana_spent

                # Boss attacks
                boss_state.boss_turn()

                # Check if player is dead
                if not boss_state.is_player_dead():
                    heapq.heappush(pq, (boss_state.mana_spent, counter, boss_state))
                    counter += 1

    return float("inf")


def parse(data):
    lines = data.strip().split("\n")
    boss_hp = int(lines[0].split(": ")[1])
    boss_damage = int(lines[1].split(": ")[1])
    return boss_hp, boss_damage


def part_one(data):
    boss_hp, boss_damage = data
    initial_state = GameState(boss_hp=boss_hp, boss_damage=boss_damage)
    return find_min_mana(initial_state)


def part_two(data):
    boss_hp, boss_damage = data
    initial_state = GameState(boss_hp=boss_hp, boss_damage=boss_damage, hard_mode=True)
    return find_min_mana(initial_state)


# Answers
# ==========================================================================
solve(part_one, parse)
solve(part_two, parse)
