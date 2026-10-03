from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ColonyGame:
    """A tiny incremental ant colony sim prototype."""

    food: int = 10
    workers: int = 2
    soldiers: int = 1
    larvae: int = 0
    nest_level: int = 1
    queen_health: int = 100
    enemy_pressure: int = 1
    turn: int = 0
    last_event: str = "The queen wakes the colony."
    game_over: bool = False

    def __post_init__(self) -> None:
        self.food = max(0, self.food)
        self.workers = max(1, self.workers)
        self.soldiers = max(1, self.soldiers)
        self.nest_level = max(1, self.nest_level)

    @property
    def worker_cost(self) -> int:
        return 12 + self.workers * 7

    @property
    def soldier_cost(self) -> int:
        return 16 + self.soldiers * 9

    @property
    def nest_cost(self) -> int:
        return 22 + self.nest_level * 18

    @property
    def food_per_tick(self) -> int:
        return self.workers * (1 + self.nest_level)

    def tick(self) -> None:
        if self.game_over:
            return
        self.turn += 1
        self.food += self.food_per_tick
        if self.turn % 6 == 0 and self.soldiers == 0:
            self.food = max(0, self.food - self.enemy_pressure * 3)
            self.last_event = "The colony is under siege and no soldiers are defending it."
        elif self.turn % 6 == 0:
            self.food += self.soldiers * 2
            self.last_event = "Workers bring food back to the nest while soldiers keep watch."
        else:
            self.last_event = "The colony is busy expanding its tunnels and gathering resources."

    def hire_worker(self) -> bool:
        if self.food < self.worker_cost:
            self.last_event = "Not enough food to hire a new worker."
            return False

        self.food -= self.worker_cost
        self.workers += 1
        self.last_event = "A new worker ant joins the colony."
        return True

    def recruit_soldier(self) -> bool:
        if self.food < self.soldier_cost:
            self.last_event = "Not enough food to train a soldier."
            return False

        self.food -= self.soldier_cost
        self.soldiers += 1
        self.last_event = "A soldier ant has been trained for defense."
        return True

    def upgrade_nest(self) -> bool:
        if self.food < self.nest_cost:
            self.last_event = "The nest needs more food before it can expand."
            return False

        self.food -= self.nest_cost
        self.nest_level += 1
        self.last_event = "The nest grows deeper and more efficient."
        return True

    def battle(self) -> bool:
        if self.game_over:
            return False

        if self.soldiers >= self.enemy_pressure:
            reward = 12 + self.enemy_pressure * 5
            self.food += reward
            self.enemy_pressure = max(1, self.enemy_pressure - 1)
            self.last_event = f"Your soldiers won the clash and brought back {reward} food."
            return True

        damage = self.enemy_pressure - self.soldiers + 1
        self.queen_health = max(0, self.queen_health - damage * 8)
        self.food = max(0, self.food - damage * 6)
        self.enemy_pressure += 1
        self.last_event = "The colony was attacked and lost ground."

        if self.queen_health <= 0:
            self.game_over = True
            self.last_event = "The queen has fallen. The colony is lost."
        return False

    def status(self) -> str:
        lines = [
            "Ant Colony Status",
            f"Food: {self.food}",
            f"Workers: {self.workers}",
            f"Soldiers: {self.soldiers}",
            f"Nest Level: {self.nest_level}",
            f"Queen Health: {self.queen_health}",
            f"Enemy Pressure: {self.enemy_pressure}",
            f"Food per tick: {self.food_per_tick}",
            f"Last event: {self.last_event}",
        ]
        return "\n".join(lines)

    def run_command(self, raw_command: str) -> str:
        command = (raw_command or "").strip().lower()
        if not command:
            return "No command entered. Try 'help'."

        if command in {"help", "?"}:
            return (
                "Commands: status, tick, gather, hire worker, train soldier, "
                "upgrade nest, battle, help, quit"
            )

        if command in {"status", "stats"}:
            return self.status()

        if command in {"tick", "gather", "advance"}:
            self.tick()
            return self.status()

        if command in {"hire worker", "hire", "worker"}:
            self.hire_worker()
            return self.status()

        if command in {"train soldier", "soldier"}:
            self.recruit_soldier()
            return self.status()

        if command in {"upgrade nest", "nest", "upgrade"}:
            self.upgrade_nest()
            return self.status()

        if command in {"battle", "raid"}:
            self.battle()
            return self.status()

        if command in {"quit", "exit"}:
            raise SystemExit

        return "Unknown command. Type 'help' for a list of actions."


def main() -> None:
    game = ColonyGame()
    print("Welcome to the Ant Colony Sim.")
    print("Type 'help' to see commands.")

    while True:
        try:
            command = input("colonies> ")
        except KeyboardInterrupt:
            print("\nSession ended.")
            break

        try:
            result = game.run_command(command)
        except SystemExit:
            print("Goodbye.")
            break

        print(result)
        if game.game_over:
            print("The colony has fallen. Starting a fresh colony...")
            game = ColonyGame()


if __name__ == "__main__":
    main()
