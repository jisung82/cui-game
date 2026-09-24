from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    hp: int = 100
    max_hp: int = 100
    gold: int = 0


@dataclass
class GameState:
    player: Player
    turn: int = 1
    running: bool = True
    log: list[str] = field(default_factory=list)


class Game:
    def __init__(self, state: GameState) -> None:
        self.state = state

    @classmethod
    def new_game(cls) -> "Game":
        return cls(GameState(player=Player(name="Player")))

    def run(self) -> None:
        self._println("=== CUI GAME ===")
        self._println("Commands: help, status, look, wait, quit")

        while self.state.running:
            command = input("> ").strip().lower()
            self.handle_command(command)

    def handle_command(self, command: str) -> str:
        if command in {"help", "?"}:
            return "help: help, status, look, wait, quit"
        if command == "status":
            p = self.state.player
            return f"{p.name} | HP {p.hp}/{p.max_hp} | Gold {p.gold} | Turn {self.state.turn}"
        if command == "look":
            return "A quiet room surrounds you. Nothing attacks you yet."
        if command == "wait":
            self.state.turn += 1
            message = f"You wait. Turn {self.state.turn}."
            self.state.log.append(message)
            return message
        if command in {"quit", "exit"}:
            self.state.running = False
            return "Goodbye."
        if command == "":
            return ""
        return f"Unknown command: {command}"

    @staticmethod
    def _println(message: str) -> None:
        if message:
            print(message)

